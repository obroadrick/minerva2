# Add access to the modules in this repo...
import sys
sys.path.append("../..")

from sigma import sigma
from kmin_bravo import kmin_bravo
from round_size_bravo import round_size_bravo

alpha = .1

p_1 = .6
p_0 = .5
sprob = .9

r = 1
n = 100
k = 57
print("\nround 1")
print("sigma:", sigma(k, n, p_1, p_0))

r=2
n=200
k=112
print("\nround 2")
print("sigma:", sigma(k, n, p_1, p_0))

r=3
n=400
k=226
print("\nround 2")
print("sigma:", sigma(k, n, p_1, p_0))

