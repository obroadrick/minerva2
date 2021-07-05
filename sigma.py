from scipy.stats import binom

def sigma(k, n, p_1, p_0):
    num = binom.pmf(k,n,p_1)
    denom = binom.pmf(k,n,p_0)
    return num / denom
