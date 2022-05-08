"""
As a function of risk limit and round size, the first round Minerva 1.0 kmin is found via search.
To save time in utilities that need to know the same kmins many times over, it may be useful to have a look-up table
for such kmins. 

This script generates such a look-up table.
"""

import numpy as np
from kmin_minerva import kmin_minerva
from tqdm import tqdm

# for now, we generate this table for a fixed contest,
# the presidenital contest in pennsylvania in 2020
biden = 3458229
trump = 3377674
margin = (biden - trump) / (trump + biden) # announced margin
p1 = biden / (trump + biden) # announced proportion of winner votes
p0 = .5 # tie


""" table for various round sizes and various risks
riskdelta = .01
risk_min = 0 + riskdelta
risk_max = 1 # always between zero and 1... i checked this/did a lil proof for it... in email inbox with subject 'risk range'
rsize_min = 100
rsize_max = 100000
rsizedelta = 10
for alpha in tqdm(np.arange(risk_min, risk_max+riskdelta, riskdelta)):
    #for round_size in tqdm(np.arange(rsize_min, rsize_max+1, rsizedelta)): #tqdm
    for round_size in np.arange(rsize_min, rsize_max+1, rsizedelta):
        kmin = kmin_minerva(round_size, p1, p0, alpha)
"""


""" table (row) just for various risks but a fixed round size """
riskdelta = .001
risk_min = 0 + riskdelta
risk_max = 1 # always between zero and 1... i checked this/did a lil proof for it... in email inbox with subject 'risk range'
rsize = 10000
kmins = np.zeros(int(1 / riskdelta)) - 1 # a -1 will denote 'no kmin exists' (or an error in general)
for alpha in tqdm(np.arange(risk_min, risk_max+riskdelta, riskdelta)):
    kmin = kmin_minerva(rsize, p1, p0, alpha)
    kmins[int(alpha * (risk_max - risk_min) / riskdelta) - 1] = kmin


""" save the kmin table for use elsewhere"""
fname = 'kmins-'+str(int(1 / riskdelta))+'riskdivs.npy'
np.save(fname, kmins)






