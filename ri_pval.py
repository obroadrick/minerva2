from sigma import sigma
from omega import omega
from kmin_bravo import kmin_bravo
from kmin_minerva2 import kmin_minerva2
from round_size_bravo import round_size_bravo
from round_size_minerva2 import round_size_minerva2
import numpy as np
import pandas as pd

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
import matplotlib.pyplot as plt

plt.plot(1 / np.array(sigmas), 'b.')
for r, c in zip([.1, .05], ['g', 'r']):
    plt.axhline(r, label='{}'.format(r), linestyle='--', color=c)
plt.ylim(0,1)

plt.legend()
plt.show()



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









