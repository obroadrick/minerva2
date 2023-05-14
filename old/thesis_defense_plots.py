""" 
Generates some plots for Oliver's thesis for a toy example audit to develop
intuition for the Minerva audit.. 
"""
import matplotlib.pyplot as plt
import numpy as np
import statistics
import math
from scipy.stats import binom
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams['text.usetex'] = True

from r2b2.simulator import DBInterface
from r2b2.simulator import histogram
from r2b2.tests.util import parse_election
from r2b2.contest import Contest
from r2b2.contest import ContestType
from kmin_bravo import kmin_bravo
from kmin_minerva import kmin_minerva
from sigma import sigma
from omega import omega
import json

# audit-specific items:
all_audit_specific_items = {}
audits = []
audit_labels = {}

# data
marker = 'o'
color = 'b'
linestyle = '-'
audit_label = r'\textsc{Providence}'
font = {'size'   : 17}
plt.rc('font', **font)
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
plt.xlabel('k_2\'')
plt.ylabel('Probability')
plt.tight_layout()
plt.legend(loc='upper left')
#plt.savefig('/Users/oliverbroadrick/Desktop/figs/justalt.png', bbox_inches='tight')
plt.show()
#plt.close(fig)
# both distributions
plt.plot(ks, p_alt, linestyle='-', color='g',label=r'$H_a$')
plt.plot(ks, p_null, linestyle='-', color='r',label=r'$H_0$')
#plt.plot([kmin_b ], [binom.pmf(kmin_b,n,p1)], color='g',marker='X',markersize=10)
#plt.plot([kmin_b ], [binom.pmf(kmin_b,n,p0)], color='r',marker='X',markersize=10)
#plt.vlines(kmin_b,0,.09, label=r'\textsc{BRAVO} $k_{min}=64$', linestyle='--',color='k')
plt.xlabel(r'$k_{2}^{m}$')
plt.ylabel('Probability')
plt.tight_layout()
plt.legend(loc='upper left')
#plt.savefig('/Users/oliverbroadrick/Desktop/figs/bothdists.png', bbox_inches='tight')
plt.show()
exit()

# some value of k
plt.plot(ks, p_alt, linestyle='-', color='g',label=r'$H_a$')
plt.plot(ks, p_null, linestyle='-', color='r',label=r'$H_0$')
kmin_b = kmin_bravo(1, n, 0, 0, p1, p0, alpha)
kmin_m = kmin_minerva(n, p1, p0, alpha)

k = 62
print('for k='+str(k)+' bravo ratio is ' + str(sigma(k, n, p1, p0)))
print('for k='+str(k)+' minerva ratio is ' + str(omega(1, k, n, 0,0,p1, p0)))

plt.plot([k], [binom.pmf(k,n,p1)], color='g',marker='X',markersize=10)
plt.plot([k], [binom.pmf(k,n,p0)], color='r',marker='X',markersize=10)
plt.vlines(k,0,.09, label=r'$k=62$', linestyle='--',color='k')
plt.xlabel('Winner votes')
plt.ylabel('Probability')
plt.tight_layout()
plt.legend(loc='upper left')
plt.savefig('/Users/oliverbroadrick/Desktop/figs/withk.png', bbox_inches='tight')
plt.show()

# Minerva plot
plt.plot(ks, p_alt, linestyle='-', color='g',label=r'$H_a$')
plt.plot(ks, p_null, linestyle='-', color='r',label=r'$H_0$')
print('for k='+str(k)+' minerva ratio is ' + str(omega(1,k, n, 0,0,p1, p0)))
plt.fill_between(ks[k:], p_alt[k:], facecolor='green', alpha=0.5)
plt.fill_between(ks[k:], p_null[k:], facecolor='red', alpha=0.5)
plt.vlines(k,0,.09, label=r'$k=62$', linestyle='--',color='k')
plt.xlabel('Winner votes')
plt.ylabel('Probability')
plt.tight_layout()
plt.legend(loc='upper left')
plt.savefig('/Users/oliverbroadrick/Desktop/figs/tails.png', bbox_inches='tight')
plt.show()

