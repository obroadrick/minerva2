from sigma import sigma
from omega import omega

# inefficient linear search... just for quick testing
def kmin_bravo(r, mnew, kprev, nprev, p_1, p_0, alpha):
    for k_ in range(kprev,kprev+mnew+1): #for each possible k
        # check if this k would pass the stopping condition
        if sigma(k_, nprev+mnew, p_1, p_0) >= 1/alpha:
            return k_
