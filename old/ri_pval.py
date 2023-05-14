from sigma import sigma
from omega import omega
from kmin_bravo import kmin_bravo
import random
random.seed(8)
from kmin_minerva2 import kmin_minerva2
from kmin_minerva import kmin_minerva
from round_size_bravo import round_size_bravo
from round_size_minerva2 import round_size_minerva2
import numpy as np
import pandas as pd
from scipy.stats import binom
import matplotlib.pyplot as plt
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams['text.usetex'] = True
font = {'size'   : 17}
plt.rc('font', **font)
# Parameters
margin = .256767
p1 = (margin + 1) / 2
p0 = .5
alpha = .1
########################################################
# get data from rhode island pilot
filename = 'interim-report.csv'
df = pd.read_csv(filename)
df.head()
df = df.sort_values(by="Ticket Numbers", ascending=True)
df.to_csv('Selection-Ordered-Sample.csv', index=False) 
approve_so = []
reject_so = []
for item in df["Audit Result"]:
    if item == 'Approve':
        approve_so.append(1)
        reject_so.append(0)
    elif item == 'Reject':
        reject_so.append(1)
        approve_so.append(0)
sample = {
    'Approve': sum(approve_so),
    'Reject': sum(reject_so),
    'Approve_so': approve_so,
    'Reject_so': reject_so,
}
########################################################

print("alpha="+str(alpha)+"  ")
print("p1="+str(p1)+"  ")
print("p0="+str(p0)+"  ")
print(" ")

# Let's see the bravo pvalue at each sequentially drawn ballot
sigmas = []
for n in range(1,140+1):
    k = sum(sample['Approve_so'][0:n])
    sig = sigma(k, n, p1, p0)
    if sig > 0:
        sigmas.append(sig)
    else:
        print(sig)

plt.plot(np.array(sigmas), 'b.')
#for r, c in zip([1/.1, 1/.05], ['g', 'r']):
plt.axhline(1/.05, label=r'$\alpha^{-1}=(0.05)^{-1}$', linestyle='-', color='r')
plt.axhline(1/.1, label=r'$\alpha^{-1}=(0.1)^{-1}$', linestyle='--', color='g')
#plt.ylim(0,1)
plt.xlabel('Sample size')
plt.ylabel(r'\textsc{BRAVO} ratio, $\sigma$')
plt.title(r'\textsc{BRAVO} ratio ($\sigma$) for pilot audit selection order')

plt.legend()
plt.subplots_adjust(bottom=0.15)
plt.show()



"""
# Now let's see the bravo kmin vs actual k in each sequential ballot draw
kmins = []
ks = []
for n in range(1,140+1):
    k = sum(sample['Approve_so'][0:n])
    ks.append(k)
    #def kmin_bravo(r, mnew, kprev, nprev, p_1, p_0, alpha):
    kmin = kmin_bravo(1, n, 0, 0, p1, p0, alpha)
    kmins.append(kmin)

plt.plot(kmins, 'r.', label='kmins')
plt.plot(ks, 'bx', label='k drawn')

plt.legend()
plt.show()
"""



##############################
marker = 'o'
color = 'b'
linestyle = '-'
"""
audit_label = r'\textsc{Providence}'
n=50
ks = np.linspace(0, n, n+1)
N = 1000
p0 = .5
p1 = .7
p_alt = binom.pmf(ks, n, p1)
p_null = binom.pmf(ks, n, p0)
alpha = .1
kmin_b = kmin_bravo(1, n, 0, 0, p1, p0, alpha)
kmin_m = kmin_minerva(n, p1, p0, alpha)
#print('for kmin='+str(kmin_b)+' bravo ratio is ' + str(sigma(kmin_b, n, p1, p0)))
#print('for kmin-1='+str(kmin_b-1)+' bravo ratio is ' + str(sigma(kmin_b-1, n, p1, p0)))

# just alternative
fig = plt.plot(ks, p_alt, linestyle='-', color='g',label=r'$H_a$')
#plt.plot(ks, p_null, linestyle='-', color='r')
#plt.plot([kmin_b ], [binom.pmf(kmin_b,n,p1)], color='g',marker='X',markersize=10)
#plt.plot([kmin_b ], [binom.pmf(kmin_b,n,p0)], color='r',marker='X',markersize=10)
#plt.vlines(kmin_b,0,.09, label=r'\textsc{BRAVO} $k_{min}=64$', linestyle='--',color='k')
plt.xlabel(r'$k_2^m$')
plt.ylabel('Probability')
plt.tight_layout()
plt.legend(loc='upper left')
#plt.savefig('/Users/oliverbroadrick/Desktop/figs/justalt.png', bbox_inches='tight')
plt.show()
"""
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams['text.usetex'] = True
font = {'size'   : 17}
plt.rc('font', **font)

fig, (ax1, ax2) = plt.subplots(2,1)
fig.suptitle(r'SO \textsc{BRAVO} Misleading Sequences')
#
##############################
kmins = []
ks = []
for n in range(1,140+1):
    k = sum(sample['Approve_so'][0:n])
    ks.append(k)
    #def kmin_bravo(r, mnew, kprev, nprev, p_1, p_0, alpha):
    kmin = kmin_bravo(1, n, 0, 0, p1, p0, alpha)
    kmins.append(kmin)

ns = np.arange(1,141)
pt = 11
pathological_ks = list(np.arange(1,pt)) + [pt]*(141-pt)
ax1.plot(ns,kmins, 'b-', label=r'\textsc{BRAVO} $k_{min}$')
ax1.plot(ns,pathological_ks, '.-', color='darkorange',label='Sample')
#ax1.plot(ns, ns/2,'--', color='green',label='Half the sample size')
ax1.plot(ns, p0*ns,'--', color='red',label=r'$p_0n$')
ax1.plot(ns, p1*ns,linestyle='dotted', color='green',label=r'$p_an$')
#ax1.set_xlabel('Sample size')
#ax1.set_ylabel('Winner ballots')
kmins = []
ks = []
for n in range(1,140+1):
    k = sum(sample['Approve_so'][0:n])
    ks.append(k)
    #def kmin_bravo(r, mnew, kprev, nprev, p_1, p_0, alpha):
    kmin = kmin_bravo(1, n, 0, 0, p1, p0, alpha)
    kmins.append(kmin)


ax1.legend(loc='upper left', handlelength=.8, labelspacing=.3)

ns = np.arange(1,141)
print(kmins)
pt = 11
pathological_ks = list(np.arange(1,pt))
for i in range(141-pt):
    if random.randint(0,1) == 0:
        pathological_ks = pathological_ks + [pathological_ks[-1]]
    else:
        pathological_ks = pathological_ks + [pathological_ks[-1]+1]


ax2.plot(ns,kmins, 'b-',label=r'\textsc{BRAVO} $k_{min}$')
ax2.plot(ns,pathological_ks, '.-', color='darkorange',label='Sample')
p0=.5
ax2.plot(ns, p0*ns,'--', color='red',label=r'$p_0n$')
ax2.plot(ns, p1*ns,linestyle='dotted', color='green',label=r'$p_an$')
ax2.set_xlabel('Sample size, n')
#ax2.set_ylabel('Winner ballots')
#plt.ylabel('Winner ballots')
fig.text(0.04, 0.5, 'Winner ballots', va='center', rotation='vertical')
plt.subplots_adjust(bottom=0.15)

plt.show()





