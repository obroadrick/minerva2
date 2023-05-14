from kmin_minerva2 import kmin_minerva2
from kmin_minerva import kmin_minerva

# Try out all these functions on an example audit

# Parameters
p_1 = .6
p_0 = .5
alpha = .1

# First round
r = 1
n1 = 125
for n in range(50,250):
    print(n)
    assert kmin_minerva(n1, p_1, p_0, alpha) == kmin_minerva2(r, n1, 0, 0, p_1, p_0, alpha)
