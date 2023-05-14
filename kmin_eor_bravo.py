from sigma import sigma
from omega import omega

# inefficient linear search... just for quick testing
def kmin_eor_bravo(r, mnew, kprev, nprev, p_1, p_0, alpha):
    for k_ in range(kprev,kprev+mnew+1): #for each possible k
        # check if this k would pass the stopping condition
        if sigma(k_, nprev+mnew, p_1, p_0) >= 1/alpha:
            return k_


# many kmins at once (will find all kmins from 1 up to roundsize
def kmins_bravo(r, n, p_1, p_0, alpha):
    kmins = []
    for n_ in range(1,n+1):
        for k in range(1, n_): #for each possible k in a round of size n_
            # check if this k would pass the stopping condition
            if sigma(k, n_, p_1, p_0) >= 1/alpha:
                kmins.append(k)
                break
        if len(kmins) < n_:
            # there is no possible kmin in this round
            kmins.append(-1) 
    return kmins
