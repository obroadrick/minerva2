# Add access to the modules in this repo...
import sys
sys.path.append("../..")

from sigma import sigma
from omega import omega
from kmin_bravo import kmin_bravo
from kmin_minerva2 import kmin_minerva2
from round_size_bravo import round_size_bravo
from round_size_minerva2 import round_size_minerva2
""" test_execute_round
contest = Contest(100000, {'A': 60000, 'B': 40000}, 1, ['A'], ContestType.MAJORITY)
minerva = Minerva2(.1, .1, contest)
assert not minerva.execute_round(100, {'A': 57, 'B': 43})
assert not minerva.stopped
assert minerva.sample_ballots['A'] == [57]
assert minerva.sample_ballots['B'] == [43]
assert not minerva.sub_audits['A-B'].stopped
assert minerva.rounds == [100]
assert not minerva.execute_round(200, {'A': 111, 'B': 89})
assert not minerva.stopped
assert minerva.sample_ballots['A'] == [57, 111]
assert minerva.sample_ballots['B'] == [43, 89]
assert not minerva.sub_audits['A-B'].stopped
assert minerva.rounds == [100, 200]
assert minerva.execute_round(400, {'A': 221, 'B': 179})
assert minerva.stopped
assert minerva.sample_ballots['A'] == [57, 111, 221]
assert minerva.sample_ballots['B'] == [43, 89, 179]
assert minerva.sub_audits['A-B'].stopped
assert minerva.rounds == [100, 200, 400]
assert minerva.get_risk_level() < 0.1
"""
p_1 = .6
p_0 = .5
alpha = .1
n1 = 100
n2 = 200
n3 = 400
k1 = 57
k2 = 111
k3 = 221

print("round 1:",omega(1, k1, n1, 0, 0, p_1, p_0))
print("round 2:",omega(2, k2-k1, n2-n1, k1, n1, p_1, p_0))
print("round 3:",omega(3, k3-k2, n3-n2, k2, n2, p_1, p_0))






