"""
As a function of risk limit and round size, the first round Minerva 1.0 kmin is usually found via search.
To save time in utilities that need to know the same kmins many times over, it may be useful to have a look-up table
for such kmins. This script generates such a look-up table.
"""

import numpy as np
from kmin_minerva import kmin_minerva
from tqdm import tqdm

# for now, we generate this look-up table for the margin of the presidential race in Pennsylvania 2020
margin = 0.01178410518 #from https://en.wikipedia.org/wiki/2020_United_States_presidential_election_in_Pennsylvania
rel_ballots = 6835903 #also from above (3,458,229 and 3,377,674)
p0 = .5
p1 = (1+margin)/2

# risk limits
risk_step = 10**(-4)
risk_min = 0 + risk_step
risk_max = 1
#risklims = np.arange(risk_min, risk_max, risk_step)
risklims = np.arange(risk_max, risk_min, (-1)*risk_step)

# round sizes
"""
rsize_min = 1000 #for fewer ballots, searches will be used rather than the look-up table
rsize_max = 6835903 // 10
rsize_step = 10
rsizes = np.arange(rsize_min, rsize_max+1, rsize_step)
"""
# for now, we can cheat with round sizes since we know that for initial testing, 
# we will just consider the case of constant round size...

# allocate table for kmins
kmins = np.zeros((len(risklims), len(rsizes))) - 1

# find kmins
for i, risk_limit in enumerate(tqdm(risklims)):
    for j, round_size in enumerate(tqdm(rsizes, leave=False)):
        kmins[i][j] = kmin_minerva(round_size, p1, p0, risk_limit)
