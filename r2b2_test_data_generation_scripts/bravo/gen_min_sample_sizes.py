# Add access to the modules in this repo...
import sys
sys.path.append("../..")

from sigma import sigma
from kmin_bravo import kmin_bravo
from round_size_bravo import round_size_bravo

min_sprob = 10**(-6)  # constant in r2b2 as minimum acceptable sprob
r = 0
k = 0
n = 0

p_1 = .6
p_0 = .5
alpha = .1

print("bravo1:", round_size_bravo(r, k, n, p_1, p_0, alpha, min_sprob))

p_1 = .51
p_0 = .5
alpha = .05

print("bravo2:", round_size_bravo(r, k, n, p_1, p_0, alpha, min_sprob))

