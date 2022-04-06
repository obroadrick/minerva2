from kmin_minerva import kmin_minerva
import numpy as np

p0 = .5
biden = 3458229
trump = 3377674
margin = (biden - trump) / (trump + biden) # announced margin
p1 = biden / (trump + biden) # announced proportion of winner votes
p0 = .5 # tie
alpha = .1 # risk limit
n = 10000
print(kmin_minerva(n, p1, p0, alpha))
