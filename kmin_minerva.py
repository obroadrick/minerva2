import math
from scipy.stats import binom
from omega import omega

def kmin_minerva(n, p1, p0, alpha):
    """ finds kmin for the first round of a minerva audit 
    
    Arguments - 
        n       : round size
        p1      : announced proportion of ballots for the winner
        p0      : proportion of ballots for the winner under the null hypothesis (.5, a tie, in the usual polling case)
        alpha   : risk limit 

    Returns - 
        kmin    : the minimum number of winner ballots for the audit to stop in the first round
                  and returns -1 if no such 1 <= kmin <= n exists
    """
    # binary search
    left = int(math.floor(n / 2) + 1)
    right = n

    # first check that the audit passes if n winner ballots are found 
    passes = omega(1, n, n, 0, 0, p1, p0) >= 1/alpha
    if not passes:
        return -1

    kmin = binary(left, right, n, p1, p0, alpha)
    return kmin

    """ old code
    # inefficient linear search... just for quick testing
    for d_ in range(0,mnew+1): #for each possible d (marginal k)
        # check if this k would pass the stopping condition
        if omega(r, d_, mnew, kprev, nprev, p_1, p_0) >= 1/alpha:
            return d_ + kprev
    """

def binary(left, right, n, p1, p0, alpha):
    """
    Performs a binary search to find the kmin for the given audit
    parameters between left and right. Returns -1 if no such kmin 
    exists.
    """
    if left + 1 == right:
        return right

    mid = (left + right) // 2
    passes = stopping_condition(mid,n,p1,p0,alpha)
    if passes:
        right = mid
    else: 
        left = mid
    return binary(left,right,n,p1,p0,alpha)

def stopping_condition(k, n, p1, p0, alpha):
    """ Checks the stopping condition for round-1 Minerva audit. 
        Returns True if the audit stops, False otherwise.
    """
    return omega(1,k,n,0,0,p1,p0) >= 1/alpha
