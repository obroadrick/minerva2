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

#temp
import matplotlib.pyplot as plt

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
        ValueError('lookupkmin - bad idx:',idx)
    return kmins[idx]

# FIRST ROUND
roundnum = 1
exp_num_rounds, exp_num_ballots, prob_reach_this_round = 0, 0, 1
#get kmin from lookup table and use it to compute easily the sprob
kmin1 = lookupkmin(alpha)
sprob1 = binom.sf(kmin1-1, marginal_round_size, p1)
print('round',roundnum,'sprob',sprob1)
exp_num_rounds += roundnum * sprob1
exp_num_ballots += marginal_round_size * prob_reach_this_round
print('after round '+str(roundnum)+', expected ballots '+str(exp_num_ballots)+' and expected rounds '+str(exp_num_rounds))
nprev = 0
nprev += marginal_round_size
kprevs = np.arange(nprev+1,dtype=int)
pr_kprevs = binom.pmf(kprevs, nprev, p1)
# zero out those above kmin1 (those which stop in the first round)
pr_kprevs[int(kmin1):] = 0
# going into second round we know that kprevs are just a binomial but also as above can be convolution still
#pr_kprevs = binom.pmf(kprevs, nprev, p1)

# SECOND ROUND (and beyond by induction!)# already set for each time thru this new round loop: kprevs, nprev, pr_kprevs
# for rounds 2 and on, the audit has a different behavior for each kprev (cumulative sample of previous winner ballots)
# make sure that initial values for the preceeding round are set before proceeding onto rounds 2 and on
sprobprev = sprob1
sprobs = [sprob1]
while roundnum <= MAX_ROUNDS - 1:
    roundnum += 1
    print('round',roundnum)
    n = nprev + marginal_round_size
    prob_reach2 = 1 - sum(sprobs)
    sprob2 = 0
    # for each possible previous sample, we compute the sprobs (and update the expectations accordingly)
    print('computing sprob...')
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
            #print('uhohcount, kprev, nprev, p1, p0, alphaprime, pr_kprevs[kprev], sigmaprev')
            #print(uhohcount, kprev, nprev, p1, p0, alphaprime, pr_kprevs[kprev], sigmaprev)
            # need to compute alphaprime from scratch...
            kmin = kmin_minerva(marginal_round_size, p1, p0, alphaprime)
            plt.plot(pr_kprevs)
        else:
            kmin = lookupkmin(alphaprime)
        sprob = pr_kprevs[kprev] * binom.sf(kmin-1, marginal_round_size, p1)
        sprob2 += sprob

    # now print the sprobs for this round
    #sprob2 = cond_sprob2 * prob_reach2 #sprob2 then is the 'absolute' probability that the audit stops in round 2
    sprobs.append(sprob2) #keep track of this sprob so that we can know the cumulative stopping probability
    print('round',roundnum,'sprob',sprob2)
    print('round',roundnum,'cumulative sprob',sum(sprobs))
    exp_num_rounds += roundnum * sprob2
    exp_num_ballots += n * sprob2
    print('after round '+str(roundnum)+', expected ballots '+str(exp_num_ballots)+' and expected rounds '+str(exp_num_rounds))

    # it will be necessary in the next round to know probability of getting each possible kprev: so we compute that here now
    # in minerva you can simply lop of the previous distributions tail and convolve with the marginal draw distribution,
    # but in providence you cannot do so since kmins depend on the previous value of k, and so we manually compute the distribution
    biggest_possible_k2 = nprev + marginal_round_size 
    k2s = np.arange(0,biggest_possible_k2+1,1,dtype=int) # 0 thru kmin-1 (so index is same as the kprev, nicely)
    marginal_pr_ks = binom.pmf(range(marginal_round_size+1), marginal_round_size, p1)   
    pr_k2s = np.zeros_like(k2s, dtype=float)
    k2sparsity = 50 # we skip (and then fill in approximately) a bunch of k2s in the distribution
    kprevsparsity = 50 # we skip (and then fill in approximately) a bunch of kprevs when computing pr_k2 for a particular k2
    last_pr_k2, second_to_last_pr_k2 = -1, -1
    last_k2, second_to_last_k2 = -1, -1
    print('computing probability distribution for next round...')
    stopped = 0
    for k2 in tqdm(k2s):
        if not k2 % k2sparsity == 0: 
            continue
            # for now, this continues (and later, when the next point is found, it will be filled in with an approximate value)
        lastpr, secondlastpr = 0,0
        for kprev in kprevs:
            if not kprev % kprevsparsity == 0:
                continue
                # for now, this continues (and later, when the next point is found, it will be filled in with an approximate value)
            stop = (omega(roundnum, k2 - kprev, marginal_round_size, kprev, nprev, p1, p0) >= 1/alpha)
            #print(roundnum, k2 - kprev, marginal_round_size, kprev, nprev, p1, p0
                    #omega(j,        dnew,       mnew,               kprev, nprev, p_1, p_0):
            if stop: 
                # this audit 'path' is ignored when computing probability of each kprev for the next round 
                # (since this path did not proceed to the next round)
                continue
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
                # add the number of items skipped times the approximate value for them each (the avg of the two, to get a linear approximation)
                pr_k2s[k2] += kprevsparsity * ((lastpr + secondlastpr) / 2)
                # so this is convolution-like but we are only adding the audit 'paths' which do in fact continue onto the next round
        second_to_last_pr_k2 = last_pr_k2
        second_to_last_k2 = last_k2
        last_pr_k2 = pr_k2s[k2]
        last_k2 = k2
        if not(last_k2 == -1 or second_to_last_k2 == -1):
            # fill in with an approximationg (average) between the second to last and last points found
            pr_k2s[second_to_last_k2+1:last_k2] = (second_to_last_pr_k2 + last_pr_k2) / 2
            """ prints for debugging
            if k2 >= 10000:
                print('filling in')
                plt.subplot(411)
                plt.plot(pr_k2s)#[9000:11000])
                tit = 'absolute pr[k'+str(roundnum)+'and proceed to round '+str(roundnum+1)+']... sum:'+str(sum(pr_k2s))#,'max:'+str(max(pr_k2s))+'min:'+str(min(pr_k2s))
                plt.title(tit)
                plt.subplot(412)
                plt.plot(pr_kprevs)
                tit = 'kprevs... sum:',str(sum(pr_kprevs))#,'max:'+str(max(pr_kprevs))+'min:'+str(min(pr_kprevs))
                plt.title(tit)
                plt.subplot(413)
                plt.plot(marginal_pr_ks)
                tit = 'marginal ks... sum:',str(sum(marginal_pr_ks))#,'max:'+str(max(marginal_pr_ks))+'min:'+str(min(marginal_pr_ks))
                plt.title(tit)
                plt.subplot(414)
                plt.plot(pr_k2s[9500:10500])
                plt.title('pr_k2s[9500:10500]')
                plt.show()
            """
 
    """ prints an dplots for debugging
    print('filling in')
    plt.subplot(311)
    plt.plot(pr_k2s)#[9000:11000])
    tit = 'absolute pr[k'+str(roundnum)+'and proceed to round '+str(roundnum+1)+']... sum:'+str(sum(pr_k2s))#,'max:'+str(max(pr_k2s))+'min:'+str(min(pr_k2s))
    plt.title(tit)
    plt.subplot(312)
    plt.plot(pr_kprevs)
    tit = 'kprevs... sum:',str(sum(pr_kprevs))#,'max:'+str(max(pr_kprevs))+'min:'+str(min(pr_kprevs))
    plt.title(tit)
    plt.subplot(313)
    plt.plot(marginal_pr_ks)
    tit = 'marginal ks... sum:',str(sum(marginal_pr_ks))#,'max:'+str(max(marginal_pr_ks))+'min:'+str(min(marginal_pr_ks))
    plt.title(tit)
    plt.show()

    print('sum of pdf over values of k in round',roundnum,':',sum(pr_k2s))
    """
     
    # before going back thru this loop, we need to update kprevs, nprev, and pr_kprevs
    kprevs = np.zeros(len(pr_k2s), dtype=int)
    for i in range(len(kprevs)):
        kprevs[i] = int(i)
    nprev = n
    pr_kprevs = pr_k2s
