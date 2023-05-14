"""
Rhode Island pilot preparation... testing against others' code.
"""


from sigma import sigma
from omega import omega
from kmin_bravo import kmin_bravo
from kmin_minerva2 import kmin_minerva2
from round_size_bravo import round_size_bravo
from round_size_minerva2 import round_size_minerva2

# Parameters
margin = .05
p_1 = (margin + 1) / 2
p_0 = .5
alpha = .02 #risk limit
print("alpha="+str(alpha)+"  ")
print("p_1="+str(p_1)+"  ")
print("p_0="+str(p_0)+"  ")
print(" ")

# First round
r = 1
n1 = 1632+1536
k1 = 1632
sprob = .73
print("Round 1 size to achieve {} sprob:".format(sprob)+"  ")
print("Bravo: "+str(round_size_bravo(r, 0, 0, p_1, p_0, alpha, sprob=sprob))+"  ")
print("Minerva 2.0: "+str(round_size_minerva2(r, 0, 0, p_1, p_0, alpha, sprob=sprob))+"  ")
print("Round 1 Draw: n1="+str(n1)+", k1="+str(k1)+"  ")
print("kmin_1(BRAVO)="+str(kmin_bravo(r, n1, 0, 0, p_1, p_0, alpha))+"  ")
print("kmin_1(Minerva 2.0)="+str(kmin_minerva2(r, n1, 0, 0, p_1, p_0, alpha))+"  ")
print("bravo risk="+str(1/sigma(k1, n1, p_1, p_0))+"  ")
print("minerva 2.0 risk="+str(1/omega(1, k1, n1, 0,0,p_1, p_0))+"  ")
print(" ")

# Second round
r = 2
n2 = 3425+3166
k2 = 3425
sprob = .88
print("Round 2 size to achieve {} sprob".format(sprob)+"  ")
print("Bravo: "+str(round_size_bravo(r, k1, n1, p_1, p_0, alpha, sprob=sprob))+"  ")
print("Minerva 2.0: "+str(round_size_minerva2(r, k1, n1, p_1, p_0, alpha, sprob=sprob))+"  ")
print("Round 2 Draw: n2="+str(n2)+", k2="+str(k2)+"  ")
print("kmin_2(BRAVO)="+str(kmin_bravo(r, n2-n1, k1, n1, p_1, p_0, alpha))+"  ")
print("kmin_2(Minerva 2.0)="+str(kmin_minerva2(r, n2-n1, k1, n1, p_1, p_0, alpha))+"  ")
print("bravo risk="+str(1/sigma(k2, n2, p_1, p_0))+"  ")
print("minerva 2 risk="+str(1/omega(2,k2-k1, n2-n1, k1, n1, p_1, p_0))+"  ")
print(" ")
