from omega import omega
import math
from scipy.stats import binom
"""
def omega(j, dnew, mnew, kprev, nprev, p_1, p_0):
    Computes and returns the ratio, omega, as defined for Minerva 2.0.

    Args:
        j       round number
        dnew    marginal tally of winner ballots in round j
        mnew    marginal number of relevant ballots drawn in round j
        kprev   cumulative tally of winner ballots through round j-1
        nprev   cumulative number of relevant ballots drawn through round j-1
        p_1     proportion of winner ballots as reported
        p_0     proportion of winner ballots assumed for the null hypothesis

    Returns:
        the omega ratio for the passed parameters and data
"""

p_1 = .9
p_0 = .5

# first round 
j = 1
n1 = 3
k1 = 3
omega1 = omega(j, k1, n1, 0, 0, p_1, p_0)
print(omega1)

# second round 
j = 2
n2 = 4
k2 = 4
omega2 = omega(j, k2-k1, n2-n1, k1, n1, p_1, p_0)
print(omega2)


"""
So we have a .9 sprob for drawing one more ballot but the r2b2 search will
not see this since it is only one greater than the previous round size

Sol'n: tell the binary search what the true minimum is 
Sol'n2: just check if drawing one more ballot is sufficient
"""

