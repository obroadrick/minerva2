# Add access to the modules in this repo...
import sys
sys.path.append("../..")

from sigma import sigma
from kmin_bravo import kmin_bravo
from round_size_bravo import round_size_bravo

min_sprob = 10**(-6)  # constant in r2b2 as minimum acceptable sprob
r = 0
kprev = 0
nprev = 0

p_1 = .6
p_0 = .5
alpha = .1
mnew = 200

print("bravo1:", kmin_bravo(r, mnew, kprev, nprev, p_1, p_0, alpha))

p_1 = .9
mnew = 2000

print("bravo2:", kmin_bravo(r, mnew, kprev, nprev, p_1, p_0, alpha))

