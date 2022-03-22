from sigma import sigma
from omega import omega
from kmin_bravo import kmin_bravo
from kmin_minerva2 import kmin_minerva2
from round_size_bravo import round_size_bravo
from round_size_minerva2 import round_size_minerva2
import numpy as np
from scipy.stats import binom

# if each ballot has fixed cost, and rounds have no overhead, 
# selection-ordered bravo is the most efficient method

# what if we assume a cost per round?
# there may be some balance between small rounds to achieve small
# average sample number vs large rounds to achieve fewer average number of rounds

ballotcost = 1
roundcost = 10 # mostly due to opening boxes (but also entering sample, getting decision, preparing next sample)

# one simple choice for round schedules is to have constant
# conditional stopping probability (round stopping probability)
# (such a scheme was used in the paper we just published)

# so we could do this: let's do a very coarse linear search over possible stopping
# probabilities, to see which one minimizes the total work on average
#candidate_sprobs = np.arange(.1, 1, .1)
#sprob = .9

# on the other hand, another feasible scheme is constant marginal round size
# which is another scheme that we entertained in that paper
# for instance, the marginal round size might make sense within some logistical constraints,
# in which case that same marginal round size could be more feasible than other choices
marginal_round_size = 100

# since infinite rounds might take too long, let's have a max
MAX_ROUNDS = 5

# this workload minimization only makes sense in the context of a certain audit and its parameters
# we begin with the presidenital contest in pennsylvania in 2020
# audit parameters
biden = 3458229
trump = 3377674
margin = (biden - trump) / (trump + biden) # announced margin
p1 = biden / (trump + biden) # announced proportion of winner votes
p0 = .5 # tie
alpha = .1 # risk limit

# let's compute the cost of this round schedule [marginal_round_size, marginal_round_size, ...]
# cost(round schedule) = (exp total num ballots) * (per ballot cost) + (exp num rounds) * (per ballot cost)

# FIRST ROUND
cur_round = 1
exp_num_rounds = 0
exp_num_ballots = 0
prob_reach_this_round = 1

kmin = kmin_minerva2(cur_round, marginal_round_size, 0, 0, p1, p0, alpha)
print(kmin)
sprob = binom.sf(kmin, marginal_round_size, p1)
print(sprob)

exp_num_rounds += cur_round * sprob
exp_num_ballots += marginal_round_size * sprob

nprev = 0
nprev += marginal_round_size

# SECOND ROUND
# for the next round, the audit has a different sprob depending on the previous round's cumulative sample
# so, for each of the previous samples, we compute the sprobs and update the expectations accordingly
"""
min_possible_kprev = 0
max_possible_kprev = kmin - 1
for kprev in range(min_possible_kprev, max_possible_kprev + 1):
    to do this slowly, we can search for a minerva 2 kmin
    kmin = kmin_minerva2(cur_round, marginal_round_size, kprev, nprev, p1, p0, alpha)
    sprob = binom.sf(kmin, marginal_round_size, p1)
    # to do this more quickly, we make the observation that:
    #   sigma(kprev,nprev) * tau_1(k',n') >= 1 / alpha 
    # is equivalent to
    #   tau_1(k',n') >= 1 / alpha' where alpha' = alpha / sigma(kprev,nprev)
    # so we can, for a modified risk limit, find the minerva 1.0 kmin
    # we can do so using a look-up table (for alpha, round size, what is minerva 1.0 first round kmin?)

    #kmin = lookup(risk

"""

"""
while num_rounds < MAX_ROUNDS:
    # what is the stopping probability in round cur_round?

    # TODO compute
    sprob = #TODO compute stopping probability for round cur_round drawing marginalj

    exp_num_rounds += num_rounds * (prob_reach)

    # prepare for next round
    num_rounds += 1
    prob_reach = prob_reach * (1 - sprob)

# expected number of ballots sampled
# n1, n2, n3, ... to achieve sprob is fixed for bravo and minerva 1.0, 
# so this computation is easier for them
r = 1
prob_reach = 1
while r < MAX_ROUNDS:
    #exp_num_rounds += num_rounds * (sprob * prob_reach)
    #round_size_bravo(r, k, n, p_1, p_0, alpha, sprob=.9, lower=1, upper=10**100, skip=10000):
    #bravo_size = round_size_bravo(r, 
    # NOTE this round size depends on k from the previous round, so needs to be computed as 
    # sum of (prob of each possible preceding k value times its associated next sample size)

    # compute expected current round size by summing over all possible previous k
    for k in range(n):
        bravo_size = round_size_bravo(r, k, n, p1, p0, alpha, sprob=sprob)

    exp_num_ballots += bravo_size * (sprob * prob_reach)

    # prepare for next round
    r += 1
    prob_reach = prob_reach * (1 - sprob)

# compute average number of ballots sampled for given sprob
# first round size is fixed


what if an adversary selected announced p to increase audit workload?

minimax - they choose p, we choose round schedule and risk schedule

or simply we always choose a certain p as part of the workload minimization
"""
