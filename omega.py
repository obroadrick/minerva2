from scipy.stats import binom
from sigma import sigma

def omega(j, dnew, mnew, kprev, nprev, p_1, p_0):
    """
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

    if j == 1:
        return omega1(dnew, mnew, p_1, p_0)
    else:
        return omega2(dnew, mnew, kprev, nprev, p_1, p_0)

def omega2(dnew, mnew, kprev, nprev, p_1, p_0):
    """ Computes omega for rounds j > 1. """
    sigmaprev = sigma(kprev, nprev, p_1, p_0)
    num = 0
    denom = 0
    """
    for d in range(dnew,mnew+1):
        num += binom.pmf(d, mnew, p_1)
        denom += binom.pmf(d, mnew, p_0)
    """
    # instead of above commented code, we use sf which gives 1-cdf
    num += binom.sf(dnew-1, mnew, p_1)
    denom += binom.sf(dnew-1, mnew, p_0)
    return sigmaprev * num / denom

def omega1(k, n, p_1, p_0):
    """ Computes omega for round j = 1. """
    num = 0
    denom = 0
    """
    for d in range(k,n+1):
        num += binom.pmf(d, n, p_1)
        denom += binom.pmf(d, n, p_0)
    """
    num += binom.sf(k-1, n, p_1)
    denom += binom.sf(k-1, n, p_0)
 
    if denom == 0:
        return -1
    return num / denom
