from math import sqrt,exp,pi

print(""" WELCOME HUMAN
This is THE CODE!!! here you can calculate SOMETHING!!!! :O""")

m = float(input('mass (in kg): '))

g = float(input('acceleration due to gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter): '))

t = float(input("time (in seconds)"))

p = float(input("density of fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water): "))

A = float(input("cross sectional area of projectile (in square meters): "))

C =float(input("drag constant (0.5 for sphere, 1.1 for cylinder falling on it’s side: "))
c = (1/2)*p*A*C

v = ( sqrt (( m*g )/c) ) * (1 - exp((-sqrt(m * g * c ) / m ) * t ))

tv = sqrt((m*g)/c)

print(f"The inner value of c is: {c:.3f}")

print(f"The velocity after {t} seconds is: {v:.3f}")

print(f"The terminal velocity is: {tv:.3f}")