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

# FIRST PLOT
marker = 'o'
color = 'b'
linestyle = '-'
audit_label = r'\textsc{Providence}'
font = {'size'   : 17}
plt.rc('font', **font)
n=100
ks = np.linspace(0, n, n+1)
N = 1000
p0 = .5
p1 = .7
p_alt = binom.pmf(ks, n, p1)
p_null = binom.pmf(ks, n, p0)
alpha = .1
kmin_b = kmin_bravo(1, n, 0, 0, p1, p0, alpha)
kmin_m = kmin_minerva(n, p1, p0, alpha)
print('for kmin='+str(kmin_b)+' bravo ratio is ' + str(sigma(kmin_b, n, p1, p0)))
print('for kmin-1='+str(kmin_b-1)+' bravo ratio is ' + str(sigma(kmin_b-1, n, p1, p0)))
plt.plot(ks, p_alt, linestyle='-', color='g')
#plt.plot(ks, p_null, linestyle='-', color='r')
#plt.plot([kmin_b ], [binom.pmf(kmin_b,n,p1)], color='g',marker='X',markersize=10)
#plt.plot([kmin_b ], [binom.pmf(kmin_b,n,p0)], color='r',marker='X',markersize=10)
#plt.vlines(kmin_b,0,.09, label=r'\textsc{BRAVO} $k_{min}=64$', linestyle='--',color='k')
plt.xlabel('Winner votes')
plt.ylabel('Probability')
plt.tight_layout()
plt.legend(loc='upper left')
plt.show()

# FIRST PLOT
marker = 'o'
color = 'b'
linestyle = '-'
audit_label = r'\textsc{Providence}'
font = {'size'   : 17}
plt.rc('font', **font)
n=100
ks = np.linspace(0, n, n+1)
N = 1000
p0 = .5
p1 = .7
p_alt = binom.pmf(ks, n, p1)
p_null = binom.pmf(ks, n, p0)
alpha = .1
kmin_b = kmin_bravo(1, n, 0, 0, p1, p0, alpha)
kmin_m = kmin_minerva(n, p1, p0, alpha)
print('for kmin='+str(kmin_b)+' bravo ratio is ' + str(sigma(kmin_b, n, p1, p0)))
print('for kmin-1='+str(kmin_b-1)+' bravo ratio is ' + str(sigma(kmin_b-1, n, p1, p0)))
plt.plot(ks, p_alt, linestyle='-', color='g')
plt.plot(ks, p_null, linestyle='-', color='r')
#plt.plot([kmin_b ], [binom.pmf(kmin_b,n,p1)], color='g',marker='X',markersize=10)
#plt.plot([kmin_b ], [binom.pmf(kmin_b,n,p0)], color='r',marker='X',markersize=10)
#plt.vlines(kmin_b,0,.09, label=r'\textsc{BRAVO} $k_{min}=64$', linestyle='--',color='k')
plt.xlabel('Winner votes')
plt.ylabel('Probability')
plt.tight_layout()
plt.legend(loc='upper left')
plt.show()



# FIRST PLOT
marker = 'o'
color = 'b'
linestyle = '-'
audit_label = r'\textsc{Providence}'
font = {'size'   : 17}
plt.rc('font', **font)
n=100
ks = np.linspace(0, n, n+1)
N = 1000
p0 = .5
p1 = .7
p_alt = binom.pmf(ks, n, p1)
p_null = binom.pmf(ks, n, p0)
alpha = .1
kmin_b = kmin_bravo(1, n, 0, 0, p1, p0, alpha)
kmin_m = kmin_minerva(n, p1, p0, alpha)
print('for kmin='+str(kmin_b)+' bravo ratio is ' + str(sigma(kmin_b, n, p1, p0)))
print('for kmin-1='+str(kmin_b-1)+' bravo ratio is ' + str(sigma(kmin_b-1, n, p1, p0)))
plt.plot(ks, p_alt, linestyle='-', color='g')
plt.plot(ks, p_null, linestyle='-', color='r')
plt.plot([kmin_b ], [binom.pmf(kmin_b,n,p1)], color='g',marker='X',markersize=10)
plt.plot([kmin_b ], [binom.pmf(kmin_b,n,p0)], color='r',marker='X',markersize=10)
plt.vlines(kmin_b,0,.09, label=r'\textsc{BRAVO} $k_{min}=64$', linestyle='--',color='k')
plt.xlabel('Winner votes')
plt.ylabel('Probability')
plt.tight_layout()
plt.legend(loc='upper left')
plt.show()

# SECOND PLOT
marker = 'o'
color = 'b'
linestyle = '-'
audit_label = r'\textsc{Providence}'
font = {'size'   : 17}
plt.rc('font', **font)
ks = np.linspace(0, n, n+1)
p_alt = binom.pmf(ks, n, p1)
p_null = binom.pmf(ks, n, p0)
kmin_b = kmin_bravo(1, n, 0, 0, p1, p0, alpha)
plt.plot(ks[:kmin_m-1], p_alt[:kmin_m-1], linestyle='-', color='g')
plt.plot(ks[:kmin_m-1], p_null[:kmin_m-1], linestyle='-', color='r')

#def omega(j, dnew, mnew, kprev, nprev, p_1, p_0):
print('for kmin='+str(kmin_m)+' minerva ratio is ' + str(omega(1,kmin_m, n, 0,0,p1, p0)))
print('for kmin='+str(kmin_m-1)+' minerva ratio is ' + str(omega(1,kmin_m-1, n, 0,0,p1, p0)))
plt.fill_between(ks[kmin_m:], p_alt[kmin_m:], facecolor='green', alpha=0.5)
plt.fill_between(ks[kmin_m:], p_null[kmin_m:], facecolor='red', alpha=0.5)
plt.vlines(kmin_m,0,.09, label=r'\textsc{Minerva} $k_{min}=57$', linestyle='--',color='k')
plt.xlabel('Winner votes')
plt.ylabel('Probability')
plt.tight_layout()
plt.legend(loc='upper left')
plt.show()


