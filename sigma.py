from scipy.stats import binom
import math

POS_INF = float(10**10)

"""
def sigma(k, n, p1, p0):
    num = binom.pmf(k,n,p1)
    denom = binom.pmf(k,n,p0)
    if denom == 0:
        return 0

    return num / denom
"""

def sigma(k, n, p1, p0):
    """ computing binomial probability with scipy 
        (old way, can have floating point issues for large n since pmf is small for any k)
    num = binom.pmf(k,n,p_1)
    denom = binom.pmf(k,n,p_0)
    """
    # compute in log space (ignoring the combination which cancels)
    # p1^k (1-p1)^{n-k} / (p0^k (1-p0)^{n-k})    then take log to get
    # (k)log(p1) + (n-k)log(1-p1) - ((k)log(p0) + (n-k)log(1-p0))
    logsigma = k*math.log(p1) + (n-k)*math.log(1-p1) - k*math.log(p0) - (n-k)*math.log(1-p0)

    return math.exp(logsigma)
