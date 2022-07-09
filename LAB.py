# Import libaries
from math import pi, sin, cos, sqrt
from matplotlib import pyplot as plt

def rad(x):
    a=(pi*x)/180
    return(a)

# Constants
g=9.8   # Define g (m/s^2)
dt=0.1 # Define dt (smaller is better)(s)
C=1    # Define drag coefficient (Make a guess for now, you'll investigate a better value in activity II)(?)
r=0.02237/2    # Define radius of projectile
A=pi*(r**2)    # Calculate cross-sectional area of projectile.
rho=1.02    # Define air density
m=0.0002116    # define mass of projectile (kg)

# Initial Conditions

v=10                  # Define launch speed
theta=(pi*45)/180          # Define launch angle (radians!!!)
vx=v*cos(theta)
vy=v*sin(theta)
x=0                   # Define initial location (one for x and one for y)
y=0.275                 # Define initial velocity (one for vx and one for vy)
t=0



xpts=[]     # Define list that will hold all of the x-coordinates
ypts=[]     # Define list that will hold all of the y-coordinates
vxpts=[]    # Define list that will hold all of the vx
vypts=[]    # Define list that will hold all of the vy
tpts=[]     # Define list that will hold all of the times

ax=((0.5)*rho*A*C*v*(v*cos(theta)))/m
ay=((0.5)*rho*A*C*v*(v*sin(theta)))/m +g
# Loop to calculate the flight time using Euler's equations 
while y > 0:
    v=sqrt((vy**2)+(vx**2))
    ax=((0.5)*rho*A*C*v*(vx*(theta)))/m
    ay=(((0.5)*rho*A*C*v*(vy*(theta)))/m) +g
    vx=vx -ax*dt      # Update vx
    vy=vy -ay*dt      # Update vy
    x=x+vx*dt         # update x
    y=y+vy            # updata y
    t=t+dt            # update time
    vxpts.append(vx)  # append to vx list
    vypts.append(vy)  # append to vy list
    xpts.append(x)    # append to x list
    ypts.append(y)    # append to y list
    tpts.append(t)    # append to time list
    print(x)
    
# Print the range
print(x)

#Plot the trajectory (I gave you this part of the code)

plt.figure(figsize = (10,10))
ax1 = plt.subplot(2,2,1)
ax1.plot(xpts,ypts,"r-")
ax1.set_title("Trajectory")
ax1.set_xlabel("x (m)")
ax1.set_ylabel("y (m)")


ax2 = plt.subplot(2,2,2)
ax2.plot(tpts,vypts,'g-')
ax2.set_title("Vy vs t")
ax2.set_xlabel("time (s)")
ax2.set_ylabel("Vy (m/s)")

ax3 = plt.subplot(2,2,3)
ax3.plot(tpts,ypts,'g-')
ax3.set_title("Y vs t")
ax3.set_xlabel("time (s)")
ax3.set_ylabel("height (m)")

ax4 = plt.subplot(2,2,4)
ax4.plot(tpts,vxpts,'b-')
ax4.set_title("Vx vs t")
ax4.set_xlabel("time (s)")
ax4.set_ylabel("Vx (m/s)")


plt.show()