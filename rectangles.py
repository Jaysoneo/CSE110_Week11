from math import sqrt
from matplotlib import pyplot as plt
'''A=0
r=0
hp=[]
xp=[]
for i in range(9):
    x=-2+((4*i)/8)
    h=sqrt(4-(x)**2)
    r=(1/8)*h
    A=A+r
    hp.append(A)
    xp.append(x)
    print(f'{i} -----   {x:.2f} --------{A:.2f} --------{h:.2f} ----------      {r:.2f}')
plt.plot(xp,hp,'o')
plt.show()'''
s=0
for i in range(2,258):
    s=s+3*i
print(s)