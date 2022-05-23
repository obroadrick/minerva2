from omega import omega
j = 2
nprev = 10000
kprev = 5000 #so didn't stop in round 1
mnew = 10000
dnew = 8000 #but should surely stop now in round 2
p1=.51
p0=.5
print(omega(j, dnew, mnew, kprev, nprev, p1, p0))
