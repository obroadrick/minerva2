"""
Testing find_sprob in the r2b2 implementation of Providence...
"""


from sigma import sigma
from omega import omega
from kmin_bravo import kmin_bravo
from kmin_minerva2 import kmin_minerva2
from round_size_bravo import round_size_bravo
from round_size_minerva2 import round_size_minerva2

# Parameters
# Get contest
contest_name = 'Virginia 2016 presidential contest'
tally = {'Hillary R. Clinton': 1981473, 'Donald J. Trump': 1769443, 'Gary Johnson': 118274, 'Ev    an McMullin':54054, 'Jill Stein':27638, 'All Others':33749}
reported_winner = max(tally, key=tally.get)
winner_votes = tally[reported_winner]
p_1 = 1981473 / (1981473 + 1769443)
p_0 = .5
alpha = .1 #risk limit
print("alpha="+str(alpha)+"  ")
print("p_1="+str(p_1)+"  ")
print("p_0="+str(p_0)+"  ")
print(" ")

# First round
r = 1
n1 = 200
k1 = 100
sprob = .1
#print("Minerva 2.0: "+str(round_size_minerva2(r, 0, 0, p_1, p_0, alpha, sprob=sprob))+"  ")
"""
print("Round 1 size to achieve {} sprob:".format(sprob)+"  ")
print("Bravo: "+str(round_size_bravo(r, 0, 0, p_1, p_0, alpha, sprob=sprob))+"  ")
print("Minerva 2.0: "+str(round_size_minerva2(r, 0, 0, p_1, p_0, alpha, sprob=sprob))+"  ")
print("Round 1 Draw: n1="+str(n1)+", k1="+str(k1)+"  ")
print("kmin_1(BRAVO)="+str(kmin_bravo(r, n1, 0, 0, p_1, p_0, alpha))+"  ")
print("kmin_1(Minerva 2.0)="+str(kmin_minerva2(r, n1, 0, 0, p_1, p_0, alpha))+"  ")
#print("sigma_1="+str(sigma(k1, n1, p_1, p_0))+"  ")
#print("omega_1="+str(omega(1, k1, n1, 0,0,p_1, p_0))+"  ")
print("bravo risk="+str(1/sigma(k1, n1, p_1, p_0))+"  ")
print("minerva 2.0 risk="+str(1/omega(1, k1, n1, 0,0,p_1, p_0))+"  ")
print(" ")
"""

# Second round
r = 2
n2 = 400
k2 = 200
sprob = .1
print("Minerva 2.0: "+str(round_size_minerva2(r, k1, n1, p_1, p_0, alpha, sprob=sprob))+"  ")
"""
print("Round 2 size to achieve {} sprob".format(sprob)+"  ")
print("Bravo: "+str(round_size_bravo(r, k1, n1, p_1, p_0, alpha, sprob=sprob))+"  ")
print("Minerva 2.0: "+str(round_size_minerva2(r, k1, n1, p_1, p_0, alpha, sprob=sprob))+"  ")
print("Round 2 Draw: n2="+str(n2)+", k2="+str(k2)+"  ")
print("kmin_2(BRAVO)="+str(kmin_bravo(r, n2-n1, k1, n1, p_1, p_0, alpha))+"  ")
print("kmin_2(Minerva 2.0)="+str(kmin_minerva2(r, n2-n1, k1, n1, p_1, p_0, alpha))+"  ")
#print("sigma_2="+str(sigma(k2, n2, p_1, p_0))+"  ")
#print("omega_2="+str(omega(2,k2-k1, n2-n1, k1, n1, p_1, p_0))+"  ")
print("bravo risk="+str(1/sigma(k2, n2, p_1, p_0))+"  ")
print("minerva 2 risk="+str(1/omega(2,k2-k1, n2-n1, k1, n1, p_1, p_0))+"  ")
print(" ")
"""


# Third round
r = 2
n3 = 600
k3 = 300
sprob = .1
print("Minerva 2.0: "+str(round_size_minerva2(r, k2, n2, p_1, p_0, alpha, sprob=sprob))+"  ")
"""
print("Round 3 size to achieve {} sprob:".format(sprob)+"  ")
print("Bravo: "+str(round_size_bravo(r, k2, n2, p_1, p_0, alpha, sprob=sprob))+"  ")
print("Minerva 2.0: "+str(round_size_minerva2(r, k2, n2, p_1, p_0, alpha, sprob=sprob))+"  ")
print("Round 3 Draw: n3="+str(n3)+", k3="+str(k3)+"  ")
print("kmin_3(BRAVO)="+str(kmin_bravo(r, n3-n2, k2, n2, p_1, p_0, alpha))+"  ")
print("kmin_3(Minerva 2.0)="+str(kmin_minerva2(r, n3-n2, k3, n3, p_1, p_0, alpha))+"  ")
#print("sigma_3="+str(sigma(k3, n3, p_1, p_0))+"  ")
#print("omega_3="+str(omega(3, k3-k2, n3-n2, k2, n2, p_1, p_0))+"  ")
print("bravo risk="+str(1/sigma(k3, n3, p_1, p_0))+"  ")
print("minerva 2.0 risk="+str(1/omega(3, k3-k2, n3-n2, k2, n2, p_1, p_0))+"  ")
print(" ")

"""


print("Minerva 2.0: "+str(round_size_minerva2(r, k3, n3, p_1, p_0, alpha, sprob=sprob))+"  ")
