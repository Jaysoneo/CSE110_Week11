t=0
v=0
g=9.8
C=0.000025
y=0
m=0.00048
a=(-m*g+C*(v**2))/m

for i in range(60):
    a=(-m*g+C*(v**2))/m
    v=v+a*0.01
    y=y+v*0.01
    print(f't={t:.1f}  ,v={v:.3f}   ,y={y:.3f}')
    t=t+0.01
