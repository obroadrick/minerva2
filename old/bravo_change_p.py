# k-cut method fails for small enough k if people can choose starting order and keep track of position
# What happens if you change p in a BRAVO audit
# CLIP audit numbers are wrong?

from sigma import sigma
from omega import omega
from kmin_bravo import kmin_bravo
from kmin_minerva2 import kmin_minerva2
from round_size_bravo import round_size_bravo
from round_size_minerva2 import round_size_minerva2

# Parameters
p1 = .7 # announced proportion
p0 = .5
alpha = .1
print("alpha="+str(alpha)+"  ")
print("p1="+str(p1)+"  ")
print("p0="+str(p0)+"  ")
print(" ")

# Now suppose we have a first round as below
r = 1
n1 = 100

# For this first round, what is kmin?
print("Round 1: n1="+str(n1))
print("kmin_1(BRAVO)="+str(kmin_bravo(r, n1, 0, 0, p1, p0, alpha))+"  ")
print("kmin_1(Minerva 2.0)="+str(kmin_minerva2(r, n1, 0, 0, p1, p0, alpha))+"  ")
print(" ")


# Ok, but what if we tried p1 other than the announced p1? pchosen
ps = []
bravokmins = []
minervakmins = []
sprobs = []
for pchosen in range(52, 99+1, 1):
    pchosen = pchosen / 100

    # compute kmins for bravo and minerva
    bravokmin = kmin_bravo(r, n1, 0, 0, pchosen, p0, alpha)
    minervakmin = kmin_minerva2(r, n1, 0, 0, pchosen, p0, alpha)
    print(pchosen, bravokmin, minervakmin)

    # track
    ps.append(pchosen)
    bravokmins.append(bravokmin)
    minervakmins.append(minervakmin)


# plot
from matplotlib import pyplot as plt
plt.plot(ps, bravokmins, label='bravo kmins')
plt.plot(ps, minervakmins, label='minerva kmins')
plt.legend(loc='upper right')
plt.ylabel('kmin')
plt.xlabel('chosen p (proportion of votes for winner under alternative)')
plt.show()

# is there a case when the bravo risk reported (according to the chosen p) is less than the true risk of the audit?
# a case when the true risk is above the risk limit when the reported risk is below?
# this would be a problem if software like arlo automatically changes the announced p to be used in the alternative computations

# how do see if such a case exists? well, we see that kmin is low for bravo at around .6, so let's compute
# the stopping probability if the true underyling is as announced, .8, and the used p is .6
# let's start by checking for k=kmin


# so when choosing kmin, can choose any at least as great as the neymen pearson kmin







