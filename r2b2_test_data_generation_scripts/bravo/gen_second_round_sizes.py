# Add access to the modules in this repo...
import sys
sys.path.append("../..")

from sigma import sigma
from kmin_bravo import kmin_bravo
from round_size_bravo import round_size_bravo

alpha = .1

p_1 = .6
p_0 = .5

n = 100
k = 54

r = 2
sprob = .9

print("bravo1:", round_size_bravo(r, k, n, p_1, p_0, alpha, sprob))

p_1 = 4617886 / (4504975 + 4617886) # Trump v clinton 2016 some state

n = 45081
k = 22634

r = 2
sprob = .9

print("bravo2:", round_size_bravo(r, k, n, p_1, p_0, alpha, sprob))

