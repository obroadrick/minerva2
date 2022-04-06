from kmin_minerva import kmin_minerva
from kmin_minerva2 import kmin_minerva2
import numpy as np

p0 = .5
for p1 in np.arange(.55,.65,.02):
    for alpha in np.arange(.05,.15,.03):
        for n in range(50, 150, 30):
            print(kmin_minerva(n, p1, p0, alpha))
            print(kmin_minerva2(1, n, 0, 0, p1, p0, alpha))
            assert kmin_minerva(n, p1, p0, alpha) == kmin_minerva2(1, n, 0, 0, p1, p0, alpha)
