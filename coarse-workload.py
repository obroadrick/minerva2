from sigma import sigma
from omega import omega
from kmin_bravo import kmin_bravo
from kmin_minerva import kmin_minerva
from round_size_bravo import round_size_bravo
from round_size_minerva2 import round_size_minerva2
import numpy as np
from scipy.stats import binom
from tqdm import tqdm
from scipy.signal import convolve

uhohcount = 0
# if each ballot has fixed cost, and rounds have no overhead, selection-ordered bravo is the most efficient RLA
# but since there is at least some overhead, which round schedule minimizes cost (workload)
ballotcost = 1
roundcost = 1000 # mostly due to opening boxes (but also entering sample, getting decision, preparing next sample)

# this workload minimization only makes sense in the context of a certain audit and its parameters
# we begin with the presidenital contest in pennsylvania in 2020
# audit parameters
biden = 3458229
trump = 3377674
margin = (biden - trump) / (trump + biden) # announced margin
p1 = biden / (trump + biden) # announced proportion of winner votes
p0 = .5 # tie
alpha = .1 # risk limit

# option 1: use fixed sprob and find which sprob minimizes workload
# option 2: we could use fixed marginal round sizes finding which minimizes workload
# both entertined in previous paper, we begin by trying option 2
marginal_round_size = 10000 #constant.

# since infinite rounds might take too long, let's have a max
MAX_ROUNDS = 5
# let's compute the cost of this round schedule [1*marginal_round_size, 2*marginal_round_size, ...]
# cost(round schedule) = (expec total num ballots) * (per ballot cost) + (expec num rounds) * (per ballot cost)

# kmins are computed in advance to make sprob calculations faster (can use lookup table not search)
divs = 1000
kmins = np.load('kmins-'+str(divs)+'riskdivs.npy')
def lookupkmin(risk):
    half = (1 / divs) / 2
    ith = int((risk + half) * divs)
    if ith == 0:
        idx = 0
    else:
        idx = ith - 1
    if idx >= len(kmins) or idx < 0:
        print('bad idx',idx)
    return kmins[idx]

# FIRST ROUND
roundnum = 1
exp_num_rounds, exp_num_ballots, prob_reach_this_round = 0, 0, 1
#get kmin from lookup table and use it to compute easily the sprob
kmin1 = lookupkmin(alpha)
sprob1 = binom.sf(kmin1-1, marginal_round_size, p1)
#print(kmin1)  #print(sprob1)
exp_num_rounds += roundnum * sprob1
exp_num_ballots += marginal_round_size * prob_reach_this_round
print('round',roundnum)
print('after round '+str(roundnum)+', expected ballots '+str(exp_num_ballots)+' and expected rounds '+str(exp_num_rounds))
nprev = 0
nprev += marginal_round_size
kprevs = np.arange(kmin1,dtype=int) # 0 thru kmin-1 (so index is same as the kprev, nicely)
pr_k_orig = [1] # 0 is only possible starting k value (so it occurs w prob 1)
marginal_pr_ks = binom.pmf(kprevs, nprev, p1)
pr_kprevs = convolve(pr_k_orig, marginal_pr_ks, method='direct')
# going into second round we know that kprevs are just a binomial but also as above can be convolution still
#pr_kprevs = binom.pmf(kprevs, nprev, p1)

# SECOND ROUND (and beyond by induction!)# already set for each time thru this new round loop: kprevs, nprev, pr_kprevs
# for rounds 2 and on, the audit has a different behavior for each kprev (cumulative sample of previous winner ballots)
while roundnum <= MAX_ROUNDS - 1:
    roundnum += 1
    if roundnum ==3:
        print('this is it:',max(pr_kprevs))
    print('round',roundnum)
    n = nprev + marginal_round_size
    prob_reach2 = 1 - sprob1
    cond_sprob2 = 0
    # for each possible previous sample, we compute the sprobs (and update the expectations accordingly)
    for kprev in tqdm(kprevs):
        # to do this more quickly, we make the observation that:
        #   sigma(kprev,nprev) * tau_1(k',n') >= 1 / alpha 
        # is equivalent to
        #   tau_1(k',n') >= 1 / alpha' where alpha' = alpha * sigma(kprev,nprev)
        # so we can, for a modified risk limit, find the minerva kmin
        # we do so using a precomputed look-up table to save time 
        if pr_kprevs[kprev] == 0:
            continue
        sigmaprev = sigma(kprev, nprev, p1, p0)
        alphaprime = alpha * sigmaprev
        if alphaprime >= 1:
            uhohcount += 1
            """
            print('\nuh oh',uhohcount,'alphaprime',alphaprime)
            print('sigmaprev',sigmaprev)
            print('nprev',nprev,'kprev',kprev)
            print('roundnum',roundnum)
            #exit()
            """
            # need to compute alphaprime on our own
            #print(uhohcount)
            print(alphaprime, pr_kprevs[kprev])
            kmin = kmin_minerva(marginal_round_size, p1, p0, alphaprime)
            #print('found kmin',kmin)
        else:
            kmin = lookupkmin(alphaprime)
        sprob = pr_kprevs[kprev] * binom.sf(kmin-1, marginal_round_size, p1)
        cond_sprob2 += sprob

    # now update the sprobs for this round
    print('cond_sprob2',cond_sprob2)
    sprob2 = cond_sprob2 * prob_reach2 #sprob2 then is the 'absolute' probability that the audit stops in round 2
    print('sprob2',sprob2)
    exp_num_rounds += roundnum * sprob2
    exp_num_ballots += marginal_round_size * sprob2#prob_reach2
    print('after round '+str(roundnum)+', expected ballots '+str(exp_num_ballots)+' and expected rounds '+str(exp_num_rounds))

    """ this comment is reference to the lines below it (finding sprob for each kprev for the next round to use)
    #pr_k2s = convolve(pr_kprevs, marginal_pr_ks, method='direct')
    a simple convolution here is wrong. some sequences stop and others don't and only those that don't stop should
    be considered when computing the "absolute" probability of getting a certain value of k in the next round (and it
    has not stopped yet) (in other words the probabilities we want are probabilities of k in that round while knowing that
    it won't get a value of k thru a sequence that stopped already so technically want Pr[Kj=kj and audit not stopped in rounds <j | H_a]
    """
    # it will be necessary in the next round to know probability of getting each possible kprev: so we compute that here now
    biggest_possible_k2 = nprev + marginal_round_size 
    k2s = np.arange(0,biggest_possible_k2+1,1,dtype=int) # 0 thru kmin-1 (so index is same as the kprev, nicely)
    # might save time here by doing this using some other convolution implementation
    marginal_pr_ks = binom.pmf(range(marginal_round_size+1), marginal_round_size, p1)   
    pr_k2s = np.zeros_like(k2s, dtype=float)
    k2sparsity = 100 # we skip (and then fill in approximately) a bunch of k2s in the distribution
    kprevsparsity = 100 # we skip (and then fill in approximately) a bunch of kprevs when computing pr_k2 for a particular k2
    last_pr_k2, second_to_last_pr_k2 = -1, -1
    last_k2, second_to_last_k2 = -1, -1
    for k2 in tqdm(k2s):
        if not k2 % k2sparsity == 0: 
            continue
            # for now, this continues (and later, when the next point is found, it will be filled in with an approximate value)
        lastpr, secondlastpr = 0,0
        for kprev in kprevs:
            if not kprev % kprevsparsity == 0:
                continue
                # for now, this continues (and later, when the next point is found, it will be filled in with an approximate value)
            stop = omega(roundnum, k2 - kprev, marginal_round_size, kprev, nprev, p1, p0) >= alpha
            if stop: 
                # this audit 'path' is ignored when computing probability of each k for the next round 
                # (since this path did not proceed to the next round)
                continue
            else:
                if k2 - kprev < 0 or k2 - kprev >= len(marginal_pr_ks):
                    continue
                    # this path also doesn't contribute since it's not possible 
                    # for example with round sizes 10,10 you can't get k2=15 if k1=2 since 15-2 = 13> 10=roundsize
                curpr = pr_kprevs[kprev] * marginal_pr_ks[k2 - kprev] #nice indexes :)
                #print('k2:',k2,'kprev:',kprev,'pr_kprevs[kprev]:',pr_kprevs[kprev])
                #print('k2:',k2,'k2-kprev:',k2-kprev,'marginal_pr_ks[k2-kprev]:',marginal_pr_ks[k2-kprev])
                pr_k2s[k2] += curpr 
                secondlastpr = lastpr
                lastpr = curpr
                if not(lastpr == -1 or secondlastpr == -1):
                    # add the number of items skipped times the approximate value for them each (the avg of the two endpoints)
                    pr_k2s[k2] += kprevsparsity * (lastpr + secondlastpr) / 2
                #pr[this k2] += pr[kprev] * marginal_pr[k2-kprev] 
                # so this is convolution-like but we are only adding the audit 'paths' which do in fact continue onto the next round
        second_to_last_pr_k2 = last_pr_k2
        second_to_last_k2 = last_k2
        last_pr_k2 = pr_k2s[k2]
        last_k2 = k2
        if not(last_k2 == -1 or second_to_last_k2 == -1):
            # fill in with an approximationg (average) between the second to last and last points found
            pr_k2s[second_to_last_k2+1:last_k2] = (second_to_last_pr_k2 + last_pr_k2) / 2
    # then here at the end we know the probability of each k2 and not having stopped already and we can add it to the next thing
     

    # before going back thru this loop, we need to update kprevs, nprev, and pr_kprevs
    kprevs = np.zeros(len(pr_k2s), dtype=int)
    for i in range(len(kprevs)):
        kprevs[i] = int(i)
    nprev = n
    pr_kprevs = pr_k2s
    print('max(pr_kprevs)',max(pr_kprevs))
