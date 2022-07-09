from math import pi,sin,cos,sqrt
from matplotlib import pyplot as plt
def rad(x):
    y=x/180*pi 
    return(y)

m=0.145
r=0.0375
A=pi*r**2
rho=1.2
y=1.05
theta=rad(28.5)
v=52
t=0
dt=0.01
vx=v*cos(theta)
vy=v*sin(theta)
g=9.8
x=0
xpts=[]
ypts=[]
vxpts=[]
vypts=[]
tpts=[]
while y>0:
    if v<=27:
        C=0.5
    else:
        C=1.06594-0.0264528*v +0.000203933*v**2
    ax=-(1/(2*m))*C*rho*A*vx*v
    ay=-g-(1/(2*m))*C*rho*A*vy*v
    vx=vx+ax*t
    vy=vy+ay*t
    v=sqrt(vx**2+vy**2)
    x=x+vx*t+(ax/2)*(t**2)
    y=y+vy*t+(ay/2)*(t**2)
    print(f"x={x:4.2f}    y={y:4.2f}    t={t:4.2f}  ")
    t=t+dt
    xpts.append(x)
    ypts.append(y)
    vxpts.append(vx)
    vypts.append(vy)
    tpts.append(t)
plt.plot(xpts,ypts)
plt.gca().set_aspect('equal', adjustable='box')
plt.draw()
#ax=plt.subplot(2,2,1)
#ax.plot(xpts,ypts)
#ax2=plt.subplot(2,2,2)
#ax2.plot(vxpts,tpts)
#ax3=plt.subplot(2,2,3)
#ax3.plot(vypts,tpts)
plt.show()