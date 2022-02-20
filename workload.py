from sigma import sigma
from omega import omega
from kmin_bravo import kmin_bravo
from kmin_minerva2 import kmin_minerva2
from round_size_bravo import round_size_bravo
from round_size_minerva2 import round_size_minerva2
import numpy as np

# if each ballot has fixed cost, and rounds have no overhead, 
# selection-ordered bravo is the most efficient method

# what if we assume a cost per round?
# there may be some balance between small rounds to achieve small
# average sample number vs large rounds to achieve fewer 
# average number of rounds

ballotcost = 1
roundcost = 10 #entering sample, getting decision, preparing next sample

# one simple choice for round schedules is to have constant
# conditional stopping probability (round stopping probability)
# (such a scheme was used in the paper we just published)

# let's do a very coarse linear search over possible stopping
# probabilities, to see which one minimizes the total work on average
#candidate_sprobs = np.arange(.1, 1, .1)
sprob = .9

# since infinite rounds might get old, let's have a max
MAX_ROUNDS = 3 # of course, so does 100

# this workload minimization only makes sense in the context of a certain audit and its parameters
# audit parameters
p1 = .6 # announced proportion of winner votes
p0 = .5 # tie
alpha = .1 # risk limit

#for sprob in candidate_sprobs:
# expected number of rounds 
num_rounds = 1
exp_num_rounds = 0
prob_reach = 1
while num_rounds < MAX_ROUNDS:
    exp_num_rounds += num_rounds * (sprob * prob_reach)

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


"""
what if an adversary selected announced p to increase audit workload?

minimax - they choose p, we choose round schedule and risk schedule

or simply we always choose a certain p as part of the workload minimization
"""
