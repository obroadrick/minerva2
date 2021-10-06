from scipy.stats import binom
from sigma import sigma
from omega import omega

# inefficient linear search... just for quick testing 
# r is the round number of the round for which we are computing a round size
# skip is how much to increase with each guess... so that this doesn't
# take absolute ages
def round_size_bravo(r, k, n, p_1, p_0, alpha, sprob=.9, lower=1, upper=10**100, skip=10000):
    for mnew in range(lower, upper + 1, skip):
        # find the d value with sprob to right of it in the alternative dist
        d = int(binom.ppf(1-sprob, mnew, p_1))
        # see if this value of d would be sufficient to pass the audit
        passes = sigma(k+d, n+mnew, p_1, p_0) >= 1/alpha
        if passes:
            if skip == 1:
                return n+mnew
            else:
                return round_size_bravo(r, k, n, p_1, p_0, alpha, sprob, max(mnew - 2*skip, 1), mnew, int(skip / 10))
