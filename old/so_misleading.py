"""
Rhode Island pilot preparation... testing against others' code.
"""


from sigma import sigma
from omega import omega
from kmin_bravo import kmin_bravo, kmins_bravo
from kmin_minerva2 import kmin_minerva2
from round_size_bravo import round_size_bravo
from round_size_minerva2 import round_size_minerva2
import random
random.seed(131233122)
import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams['text.usetex'] = True

font = {'size'   : 17}
plt.rc('font', **font)

# Parameters
margin = .10
p_1 = (margin + 1) / 2
p_0 = .5
alpha = .1 #risk limit
print("alpha="+str(alpha)+"  ")
print("p_1="+str(p_1)+"  ")
print("p_0="+str(p_0)+"  ")
print(" ")

# First round
r = 1
n1 = 150
k1 = 60
print("Round 1 Draw: n1="+str(n1)+", k1="+str(k1)+"  ")
print("kmin_1(BRAVO)="+str(kmin_bravo(r, n1, 0, 0, p_1, p_0, alpha))+"  ")
print("kmins(BRAVO)="+str(kmins_bravo(r, n1,  p_1, p_0, alpha))+"  ")
print("bravo risk="+str(1/sigma(k1, n1, p_1, p_0))+"  ")
print("minerva 2.0 risk="+str(1/omega(1, k1, n1, 0,0,p_1, p_0))+"  ")


kmins = kmins_bravo(r, n1,  p_1, p_0, alpha)
kminns = [i for i in range(n1+1)]
for i in range(len(kmins)):
    if kmins[i] == -1:
        kmins[i] = None

sample = [1]
# make the sample lucky
for i in range(6):
    r = random.uniform(0,1)
    if r < .73:
        #rarely find a loser ballot
        sample.append(sample[-1])
    else:
        #usually find winner ballot
        sample.append(sample[-1]+1)
# make the sample lucky
for i in range(44):
    r = random.uniform(0,1)
    if r > .73:
        #rarely find a loser ballot
        sample.append(sample[-1])
    else:
        #usually find winner ballot
        sample.append(sample[-1]+1)
# no make rest of sample unlucky
for i in range(49+50):
    r = random.uniform(0,1)
    if r < .8:
        #usually find a loser ballot
        sample.append(sample[-1])
    else:
        #rarely find winner ballot
        sample.append(sample[-1]+1)



plt.plot(range(n1), kmins, label=r'$k_{min}$')
plt.plot(range(n1), sample, label='Sample')
plt.xlabel('Number of ballots sampled, $n$')
plt.ylabel('Number of ballots for announced winner, $k$')
plt.title('Example of a \emph{misleading sequence} \n under SO '+r'\textsc{BRAVO}')
plt.legend(loc='upper left')
plt.show()






