from numpy import sin, cos, linspace, array, sqrt
from math import pi
from matplotlib import pyplot as plt

def rad(x):
    a=(x*pi)/180
    return(a)

v= 250
theta= rad(75.64)
theta1=rad(50.12)

t=0
x=0
dt=0.001
y=0
y1=0
x1=0

xpts=[]  
ypts=[] 
x3pts=[]  
y3pts=[]     
x1pts=[]  
y1pts=[]
tpts=[]
dd=2
aa=0
#print("working")
while y >=0 :  
    dd=dd+1
    x=v*cos(theta)*t          
    y=v*sin(theta)*t -4.9*(t**2)
    #if 0< y< 1:
    #    print("(",x,",",y,")")
    t=t+dt
    xpts.append(x)  
    ypts.append(y)
    
while y1 >=0 :  
    x1=v*cos(theta1)*t          
    y1=v*sin(theta1)*t -4.9*(t**2)
    t=t+dt
    x3pts.append(x1)  
    y3pts.append(y1)

#print(cc)

#if 1790< y < 1810:
#        aa=theta
#        bb=y
#        tt=t
#        if dd<5:
#            print("working ",dd)
#        while bb<1799.999 or bb>1800.001:
#            if dd<500:
#                print("working ",d)
#                dd=dd+1
#            
#            if bb<1800.001:
#                aa=aa+aa/2
#                bb=v*sin(aa)*tt -4.9*(tt**2)
#            elif bb>1799.999:
#                aa=aa-aa/2
#                bb=v*sin(aa)*tt -4.9*(tt**2)      
#print(ypts)
    

plt.figure(figsize = (20,20))
plt.plot(x3pts,y3pts,"g")
plt.plot(xpts,ypts,"r-")
plt.vlines(2500, 0, 1800)
plt.title("Trajectory")
plt.xlabel("x (m)")
plt.ylabel("y (m)")

plt.show()


# In[96]:


from math import atan,sqrt,cos,sin

g=9.8
v=250
y=1800
x=2500
A=(-g/(2*(v**2))*(x**2))
B=x
C=-y+A
D=(B**2)-4*A*C
D=sqrt(D)

t1=atan((-B+D)/(2*A))
t2=atan((-B-D)/(2*A))

t3=t1/pi*180
t4=t2/pi*180

d1=(v*cos(t1)*(2*v*sin(t1)))/g
d2=(v*cos(t2)*(2*v*sin(t2)))/g

print(f"d1= {d1:.5f}, d2= {d2:.5f}")

print(f"t1= {t1:.5f} ,t2= {t1:.5f}, t3= {t3:.5f}, t4= {t4:.5f}")