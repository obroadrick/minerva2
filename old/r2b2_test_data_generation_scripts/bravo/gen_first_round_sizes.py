# Add access to the modules in this repo...
import sys
sys.path.append("../..")

from sigma import sigma
from kmin_bravo import kmin_bravo
from round_size_bravo import round_size_bravo

r = 0
k = 0
n = 0
sprob = .9
p_0 = .5
alpha = .1

p_1 = .6

print("bravo1:", round_size_bravo(r, k, n, p_1, p_0, alpha, sprob))

p_1 = .51

print("bravo2:", round_size_bravo(r, k, n, p_1, p_0, alpha, sprob))

p_1 = 5040799 / 10000000

print("bravo3:", round_size_bravo(r, k, n, p_1, p_0, alpha, sprob))

