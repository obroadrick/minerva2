from sigma import sigma
from omega import omega
import math
import numpy as np

def so_bravo_sprob(r, mnew, kprev, nprev, p1, p0, alpha):
        """Helper method to find the stopping probability of a given prospective round size."""
        # Get current audit state and prospective marginal draw.
        p = p1
        kprev = 0
        nprev = 0
        marginal_draw = mnew

        # In BRAVO, kmin is an affine function of n.
        # We can compute the constants for this affine function to make
        # computing kmin easy.

        # Useful constant.
        logpoveroneminusp = math.log(p/(1-p))

        # Affine constants.
        intercept = math.log(1 / alpha) / logpoveroneminusp
        slope = math.log(1 / (2 - 2*p)) / logpoveroneminusp

        # Distribution over drawn winner ballots for m = 1. 
        num_dist = np.array([1 - p, p])
        
        # Maintain cumulative probability of stopping.
        kmins = []
        sprobs = []
        sprob = 0

        # For each new ballot drawn, compute the probability of meeting the 
        # BRAVO stopping rule following that particular ballot draw.
        for m in range(1, marginal_draw + 1):
            n = nprev + m

            # Compute kmin for n.
            kmin = math.ceil(intercept + n * slope)

            # The corresponding stopping probability for this round size is 
            # probability that the drawn k is at least kmin.
            draw_min = kmin - kprev
            if draw_min >= len(num_dist):
                sprob_m = 0
            else:
                sprob_m = sum(num_dist[draw_min:])
                num_dist = np.append(num_dist[0 : draw_min], np.zeros(m + 1 - draw_min))

            # Record kmin, sprob_m, and updated cumulative sprob.
            kmins.append(kmin)
            sprobs.append(sprob_m)
            sprob += sprob_m

            # Update distribution for next value of m.
            num_dist_winner_next = np.append([0], num_dist) * (p)
            num_dist_loser_next = np.append(num_dist * (1 - p), [0])
            num_dist = num_dist_winner_next + num_dist_loser_next
 
        return kmins, sprob, sprobs
