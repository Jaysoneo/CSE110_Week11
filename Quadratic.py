import math as m
from math import log10, floor

A=float(input('A='))
B=float(input('B='))
C=float(input('C='))
E1=0
E2=0
E3=0
E4=0
E5=0
D=B**2-4*A*C




if D >= 0:
    E1=(-B+m.sqrt(D))/(2*A)
    E2=(-B-m.sqrt(D))/(2*A)
    print(f"""------------------------------------
solution 1= {E1:.3f}
solution 2= {E2:.3f}
------------------------------------""")
else:
    E3=(m.sqrt(abs(D)))/(2*A)
    E4=(-m.sqrt(abs(D)))/(2*A)
    E5=(-B)/(2*A)
    print(f'solution 1= {E5:.3f}+{E4:.3f}i'
    f'\nsolution 2= {E5:.3f} {E3:.3f}i')

