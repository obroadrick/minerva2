"""
Rhode Island pilot preparation... testing against others' code.
"""


from sigma import sigma
from omega import omega
from kmin_eor_bravo import kmin_eor_bravo
from kmin_minerva2 import kmin_minerva2
from round_size_bravo import round_size_bravo
from round_size_minerva2 import round_size_minerva2
from scipy.stats import binom
import math
import numpy as np
from kmin_so_bravo import so_bravo_sprob

def misleading_pr(n, p1, p0=.5):
    """
    Computes the probability (assuming the alternative) that the loser gets more votes
    (i.e. the number of winner votes is below p0*n)
    """
    return binom.cdf(math.floor(p0*n), n, p1)

def prov_sprob(n, p1, p0, alpha):
    kmin = kmin_minerva2(1,n,0,0,p1,p0,alpha)
    return binom.sf(kmin-1,n,p1)

def so_sprob(n, p1, p0, alpha):
    kmin = kmin_so_bravo(1,n,0,0,p1,p0,alpha)
    return binom.sf(kmin-1,n,p1)

def eor_sprob(n, p1, p0, alpha):
    kmin = kmin_eor_bravo(1,n,0,0,p1,p0,alpha)
    return binom.sf(kmin-1,n,p1)

# for a misleading limit
misleading_limits = [.1, .01, .001]
results = {
    'misleading_limits':misleading_limits,
    'results':[]
}
for misleading_limit in misleading_limits:
    # for various margins
    margins = np.array([.25,.2,.15,.1,.05,.04,.03,.02,.01])#np.array(range(25,3,-1))*.01
    round_sizes = []
    for margin in margins:
        print(margin)
        p1 = (margin + 1) / 2
        p0 = .5
        alpha = .1
        # linear search for round size that achieves desired misleading probability
        for n in range(1,10**7):
            pr_misleading = misleading_pr(n, p1, p0)
            if pr_misleading < misleading_limit:
                round_sizes.append(n)
                break

    # for these round sizes, find corresponding probability of stopping for each audit
    prov_sprobs = []
    so_sprobs = []
    eor_sprobs = []
    for i in range(len(margins)):
        margin = margins[i]
        p1 = (margin + 1) / 2
        p0 = .5
        alpha = .1
        n = round_sizes[i]
        print('margin '+str(margin)+' round size '+str(n))
        prov_sprobs.append(prov_sprob(n, p1, p0, alpha))
        print('prov_sprob='+str(prov_sprobs[-1]))
        so_sprobs.append(so_bravo_sprob(1, n, 0, 0, p1, p0, alpha)[1])
        print('so_sprob='+str(so_sprobs[-1]))
        eor_sprobs.append(eor_sprob(n, p1, p0, alpha))
        print('eor_sprob='+str(eor_sprobs[-1]))

    # store results
    results['results'].append({
        'margins':list(margins),
        'min_round_sizes':list(round_sizes),
        'prov_sprobs':list(prov_sprobs),
        'so_sprobs':list(so_sprobs),
        'eor_sprobs':list(eor_sprobs)
    })

import json

with open('misleading.json','w') as f:
    json.dump(results, f)

