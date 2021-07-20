# Add access to the modules in this repo...
import sys
sys.path.append("..")

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
#print(omega(1, k1, n1, 0, 0, p_1, p_0))
n2 = 200
k2 = 113
#print(omega(2, k2-k1, n2-n1, k1, n1, p_1, p_0))
r = 3
sprob = .9
skip = 1 # initial granularity of search 
print("case 1 round size (for round 3): "+str(round_size_minerva2(r, k2, n2, p_1, p_0, alpha, sprob=sprob, skip=skip)))

# Case 2
p_1 = 4617886 / (4504975 + 4617886)
p_0 = .5
alpha = .1
n1 = 45081
k1 = 22634
print(omega(1, k1, n1, 0, 0, p_1, p_0))
n2 = 50000
k2 = 25200
print(omega(2, k2-k1, n2-n1, k1, n1, p_1, p_0))
r = 3
sprob = .9
skip = 100000# initial granularity of search 
print("case 2 round size (for round 3): "+str(round_size_minerva2(r, k2, n2, p_1, p_0, alpha, sprob=sprob, skip=skip)))
