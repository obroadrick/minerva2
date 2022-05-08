# providence
Providence is a flexible round-by-round Risk-Limiting Audit.
This is my personal code for the Providence audit. I use this repo for general exploration as well as test data generation for testing the code in [r2b2](https://github.com/gwexploratoryaudits/r2b2)...

## Example
Here is a sample of some computations that this code can perform:  

alpha=0.1  
p_1=0.6  
p_0=0.5  
 
Round 1 size to achieve 90% sprob:  
Bravo: 342  
Minerva 2.0: 173  
Round 1 Draw: n1=125, k1=70  
kmin_1(BRAVO)=75  
kmin_1(Minerva 2.0)=71  
sigma_1=1.63168570176992  
omega_1=8.009916930248211  
 
Round 2 size to achieve 90% sprob:  
Bravo: 431  
Minerva 2.0: 265  
Round 2 Draw: n2=225, k2=126  
kmin_2(BRAVO)=130  
kmin_2(Minerva 2.0)=127  
sigma_2=2.414046960617199  
omega_2=9.878411274542342  
 
Round 3 size to achieve 90% sprob:  
Bravo: 493  
Minerva 2.0: 330  
Round 3 Draw: n3=325, k3=182  
kmin_3(BRAVO)=185  
kmin_3(Minerva 2.0)=181  
sigma_3=3.571535082855545  
omega_3=14.61491553622636  
