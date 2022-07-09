
from math import pi
a=float(input('what is the size of the square in cm?:'))
CA=1/10000
CV=1/1000000
a1=a**2
a11=a**3
a12=a1*CA
a112=a11*CV
print(f"the area of the square is {a1} cm^2 or {a12}m^2")
print(f'the volume of the cube is {a11}cm^2 or {a112}m^3')

a2=float(input('what is the length of the rectangle in cm?:'))
a3=float(input('what is the with of the rectangle  in cm?:'))
a3=a3*a2
a33=a3*CA
print(f"the area of the rectangle is {a3}cm^2 or {a33}m^2")

r=float(input('what is the radius of the circle in cm?:'))
a4=pi*r**2
a41=a4*CA
a44=(4/3)*pi*(r**3)
a441=a44*CV
print(f'the area of the circle is {a4}cm^2 {a41}m^2')
print(f'the volume of the {a44} cm^3 or {a441} m^3 ')

