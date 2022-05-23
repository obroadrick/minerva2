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
    """
    numdist = binom.pmf(range(mnew),mnew,p_1)
    denomdist = binom.pmf(range(mnew),mnew,p_0)
    num = sum(numdist[dnew:])
    denom = sum(denomdist[dnew:])
    if denom == 0:
        if num == 0:
            # we are far to the right of both means to get nonzero tails
            return 10**10 # since this is sufficient evidence
        else:
            # if we are too far to the right of the null mean but maybe not to
            # the right of the alt mean, then there is great evidence here for the 
            # alt over the null
            return 10**10

    if denom == 0:
        return -1
    return num / denom
    print('how did you reach this???')
    """

    # instead of above commented code, we use sf which gives 1-cdf
    num += binom.sf(dnew-1, mnew, p_1)
    denom += binom.sf(dnew-1, mnew, p_0)
    if denom == 0:
        if num == 0:
            # we are far to the right of both means to get nonzero tails
            return 10**10 # since this is sufficient evidence
        else:
            # if we are too far to the right of the null mean but maybe not to
            # the right of the alt mean, then there is great evidence here for the 
            # alt over the null
            return 10**10

    #print(sigmaprev, num, denom)
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
    numdist = binom.pmf(range(n),n,p_1)
    denomdist = binom.pmf(range(n),n,p_0)
    num = sum(numdist[k:])
    denom = sum(denomdist[k:])
    if denom == 0:
        if num == 0:
            # we are far to the right of both means to get nonzero tails
            return 10**10 # since this is sufficient evidence
        else:
            # if we are too far to the right of the null mean but maybe not to
            # the right of the alt mean, then there is great evidence here for the 
            # alt over the null
            return 10**10

    #num = binom.sf(k-1,n,p_1)
    #denom = binom.sf(k-1,n,p_0)
    #print(num,denom)
    if denom == 0:
        return -1
    return num / denom
