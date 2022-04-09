from scipy.stats import binom
from sigma import sigma
from omega import omega

# inefficient linear search... just for quick testing 
# r is the round number of the round for which we are computing a round size
# skip is how much to increase with each guess... so that this doesn't
# take absolute ages
def round_size_minerva2(r, k, n, p_1, p_0, alpha, sprob=.9, lower=1, upper=10**100, skip=10000):
    #print("skip", skip)
    #print('called w lower=',lower,'upper=',upper,'and skip=',skip)
    for mnew in range(lower, upper + 1, skip):
        #print(n+mnew)
        # find the d value with sprob to right of it in the alternative dist
        d = int(binom.ppf(1-sprob, mnew, p_1))

        # see if this value of d would be sufficient to pass the audit
        passes = omega(r, d, mnew, k, n, p_1, p_0) >= 1/alpha
        if passes:
            if skip == 1:
                return n+mnew
            else:
                return round_size_minerva2(r, k, n, p_1, p_0, alpha, sprob, mnew - skip, mnew, int(skip / 10))
