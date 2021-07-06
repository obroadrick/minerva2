from scipy.stats import binom
from sigma import sigma
from omega import omega

# inefficient linear search... just for quick testing 
# r is the round number of the round for which we are computing a round size
def round_size_bravo(r, k, n, p_1, p_0, alpha, sprob=.9):
    for mnew in range(1, 1000): #linearly try mnew values
        # find the d value with 90% + to right of it in the alternative dist
        d = binom.ppf(1-sprob, mnew, p_1)
        # see if this value of d would be sufficient to pass the audit
        if sigma(k+d, n+mnew, p_1, p_0) >= 1/alpha:
            return n+mnew
