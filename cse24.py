from math import pi
def sq_area(x):
    'x is the side of the square, then, the area is calculated'
    y=x**2
    return y
def rec_area(x,y):
    'x is the width and y is the length of the rectangle, then, the area is calculated'
    z=x*y
    return z
def circ_area(x):
    'x is the radius of the circle, then, the area is calculated'
    y=pi*(x**2)
    return y

side=input('input the side of a square: ')
area=sq_area(float(side))
print(area)

width=input('input the width of the rectangle: ')
length=input('input the length of the rectangle: ')
area=rec_area(float(width),float(length))
print(area)

rad=input('input the radius of a circle: ')
area=circ_area(float(rad))
print(area)