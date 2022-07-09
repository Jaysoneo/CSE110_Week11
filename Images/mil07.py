from PIL import Image 
from matplotlib import numpy as n
import random


img=Image.open('earth.jpg')
img2=Image.open('cat.jpg')
earth=img.load()
cat=img2.load()

aux1=0
aux2=0

row=0
column=0


for row in range(600):
    for column in range(800):
        (r,g,b) = cat[column,row]
        if 130>r and g>150 and 130>b:
            cat[column,row] = earth[column,row]
row=0
column=0

a=0
b=0
#print the value of 5 random pixels
for i in range(5):
    a = random.randint(1, 799)
    b = random.randint(1, 599)
    for j in range(5):
        (r,g,b) = cat[a,b]
    print((r,g,b))

row=0
column=0

#Purple sky and oceans
for row in range(600):
    for column in range(800):
        (r,g,b) = cat[column,row]
        if 150>r and 150>g and 100<b:
            cat[column,row] = (r+60,g-10,b+90)
row=0
column=0
# dark filter
for row in range(600):
   for column in range(800):
        (r,g,b) = cat[column,row]
        cat[column,row] = (r-40,g-40,b-20)
img2.save("Dark_Cat_Purple_Planet.jpg")
img2.show()
