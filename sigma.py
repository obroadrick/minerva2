from scipy.stats import binom
import math

POS_INF = float(10**10)

def sigma(k, n, p_1, p_0):
    num = binom.pmf(k,n,p_1)
    denom = binom.pmf(k,n,p_0)
    if denom == 0:
        return 0

    return num / denom
