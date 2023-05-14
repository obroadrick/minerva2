from sigma import sigma
from omega import omega

# inefficient linear search... just for quick testing
def kmin_minerva2(r, mnew, kprev, nprev, p_1, p_0, alpha, kmin_lb = 0):
    """
    If a lower bound on the value of kmin is known (because perhaps the kmin
    for a smaller round size is known) then that is optionally passed to speed
    things up. Else, kmin_lb defaults to 0.
    """
    if kmin_lb is None:
        kmin_lb = 0
    for d_ in range(kmin_lb,mnew+1): #for each possible d (marginal k)
        # check if this k would pass the stopping condition
        if omega(r, d_, mnew, kprev, nprev, p_1, p_0) >= 1/alpha:
            #print(omega(r, d_, mnew, kprev, nprev, p_1, p_0))
            return d_ + kprev




