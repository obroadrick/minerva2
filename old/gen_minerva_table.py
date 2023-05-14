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
"""
biden = 3458229
trump = 3377674
margin = (biden - trump) / (trump + biden) # announced margin
p1 = biden / (trump + biden) # announced proportion of winner votes
p0 = .5 # tie
"""
#michigan
biden = 2804040
trump = 2649852
margin = (biden - trump) / (trump + biden) # announced margin
p1 = biden / (trump + biden) # announced proportion of winner votes
p0 = .5 # tie
alpha = .1 # risk limit



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
# that proof was wrong! since it assumed that bravo stop => providence stop but for rounds 3 and on that is not necessarily true
########
#rsize = 10000 ... 
sprobs = [0.95, 0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05]
first_round_sizes = [11154,8813,7425,6434,5700,5125,4599,4211,3815,3458,3181,2888,2625,2386,2129,1911,1672,1388,1117]
marginal_round_size = first_round_sizes[0] #constant.
rsize = marginal_round_size
########

kmins = np.zeros(int(1 / riskdelta)) - 1 # a -1 will denote 'no kmin exists' (or an error in general)
for alpha in tqdm(np.arange(risk_min, risk_max+riskdelta, riskdelta)):
    kmin = kmin_minerva(rsize, p1, p0, alpha)
    kmins[int(alpha * (risk_max - risk_min) / riskdelta) - 1] = kmin


""" save the kmin table for use elsewhere"""
fname = 'michigan-kmins-'+str(int(1 / riskdelta))+'riskdivs.npy'
np.save(fname, kmins)






