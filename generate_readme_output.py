from sigma import sigma
from omega import omega
from kmin_bravo import kmin_bravo
from kmin_minerva2 import kmin_minerva2
from round_size_bravo import round_size_bravo
from round_size_minerva2 import round_size_minerva2

# Try out all these functions on an example audit

# Parameters
p_1 = .6
p_0 = .5
alpha = .1
print("alpha="+str(alpha)+"  ")
print("p_1="+str(p_1)+"  ")
print("p_0="+str(p_0)+"  ")
print(" ")

# First round
r = 1
n1 = 125
k1 = int(.56*125)
print("Round 1 size to achieve 90% sprob:"+"  ")
print("Bravo: "+str(round_size_bravo(r, 0, 0, p_1, p_0, alpha))+"  ")
print("Minerva 2.0: "+str(round_size_minerva2(r, 0, 0, p_1, p_0, alpha))+"  ")
print("Round 1 Draw: n1="+str(n1)+", k1="+str(k1)+"  ")
print("kmin_1(BRAVO)="+str(kmin_bravo(r, n1, 0, 0, p_1, p_0, alpha))+"  ")
print("kmin_1(Minerva 2.0)="+str(kmin_minerva2(r, n1, 0, 0, p_1, p_0, alpha))+"  ")
print("sigma_1="+str(sigma(k1, n1, p_1, p_0))+"  ")
print("omega_1="+str(omega(1, k1, n1, 0,0,p_1, p_0))+"  ")
print(" ")

# Second round
r = 2
n2 = n1+100
k2 = k1+int(.56*(n2-n1))
print("Round 2 size to achieve 90% sprob:"+"  ")
print("Bravo: "+str(round_size_bravo(r, k1, n1, p_1, p_0, alpha))+"  ")
print("Minerva 2.0: "+str(round_size_minerva2(r, k1, n1, p_1, p_0, alpha))+"  ")
print("Round 2 Draw: n2="+str(n2)+", k2="+str(k2)+"  ")
print("kmin_2(BRAVO)="+str(kmin_bravo(r, n2-n1, k1, n1, p_1, p_0, alpha))+"  ")
print("kmin_2(Minerva 2.0)="+str(kmin_minerva2(r, n2-n1, k1, n1, p_1, p_0, alpha))+"  ")
print("sigma_2="+str(sigma(k2, n2, p_1, p_0))+"  ")
print("omega_2="+str(omega(2,k2-k1, n2-n1, k1, n1, p_1, p_0))+"  ")
print(" ")

# Third round
r = 3
n3 = n2+100
k3 = k2+int(.56*(n3-n2))
print("Round 3 size to achieve 90% sprob:"+"  ")
print("Bravo: "+str(round_size_bravo(r, k2, n2, p_1, p_0, alpha))+"  ")
print("Minerva 2.0: "+str(round_size_minerva2(r, k2, n2, p_1, p_0, alpha))+"  ")
print("Round 3 Draw: n3="+str(n3)+", k3="+str(k3)+"  ")
print("kmin_3(BRAVO)="+str(kmin_bravo(r, n3-n2, k2, n2, p_1, p_0, alpha))+"  ")
print("kmin_3(Minerva 2.0)="+str(kmin_minerva2(r, n3-n2, k2, n2, p_1, p_0, alpha))+"  ")
print("sigma_3="+str(sigma(k3, n3, p_1, p_0))+"  ")
print("omega_3="+str(omega(3, k3-k2, n3-n2, k2, n2, p_1, p_0))+"  ")
print(" ")

