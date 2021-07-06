from sigma import sigma
from omega import omega

# inefficient linear search... just for quick testing
def kmin_minerva2(r, mnew, kprev, nprev, p_1, p_0, alpha):
    for d_ in range(0,mnew+1): #for each possible d (marginal k)
        # check if this k would pass the stopping condition
        if omega(r, d_, mnew, kprev, nprev, p_1, p_0) >= 1/alpha:
            return d_ + kprev
