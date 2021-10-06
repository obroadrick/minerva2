# Add access to the modules in this repo...
import sys
sys.path.append("../..")

from sigma import sigma
from omega import omega
from kmin_bravo import kmin_bravo
from kmin_minerva2 import kmin_minerva2
from round_size_bravo import round_size_bravo
from round_size_minerva2 import round_size_minerva2

# Case 1
p_1 = .6
p_0 = .5
alpha = .1
n1 = 100
k1 = 54
r = 2
sprob = .9
skip = 1
print("round size (for round 2):"+str(round_size_minerva2(r, k1, n1, p_1, p_0, alpha, sprob, skip)))

# Case 2
p_1 = 4617886 / (4504975 + 4617886)
p_0 = .5
alpha = .1
n1 = 45081
k1 = 22634
r = 2
sprob = .9
skip = 10000
print("round size (for round 2):"+str(round_size_minerva2(r, k1, n1, p_1, p_0, alpha, sprob, skip)))
