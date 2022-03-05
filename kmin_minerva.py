import math
from scipy.stats import binom

def kmin_minerva(n, p1, p0, alpha):
    """ finds kmin for the first round of a minerva audit 
    
    Arguments - 
        n       : round size
        p1      : announced proportion of ballots for the winner
        p0      : proportion of ballots for the winner under the null hypothesis (.5, a tie, in the usual polling case)
        alpha   : risk limit 

    Returns - 
        kmin    : the minimum number of winner ballots for the audit to stop in the first round
    """
    # binary search
    lower_bound = int(math.floor(n / 2) + 1)
    upper_bound = n

    # first check that the audit passes if n winner ballots are found 

    # inefficient linear search... just for quick testing
    for d_ in range(0,mnew+1): #for each possible d (marginal k)
        # check if this k would pass the stopping condition
        if omega(r, d_, mnew, kprev, nprev, p_1, p_0) >= 1/alpha:
            return d_ + kprev
