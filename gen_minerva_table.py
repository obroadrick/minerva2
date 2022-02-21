"""
As a function of risk limit and round size, the first round Minerva 1.0 kmin is usually found via search.
To save time in utilities that need to know the same kmins many times over, it may be useful to have a look-up table
for such kmins. This script generates such a look-up table.
"""

import numpy as np

risk_step = .01
risk_min = 0 + risk_step
risk_max = 1 #this might need to be quite large, not just 1
rsize_min = 1
rsize_max = 10**5
rsize_step = 1
for risk_limit in np.arange(risk_min, risk_max+1, risk_step):
    for round_size in np.arange(rsize_min, rsize_max+1, rsize_step):
        kmin = kmin
