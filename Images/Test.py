from PIL import Image 
from matplotlib import numpy as n
img=Image.open('beach.jpg')
img2=Image.open('harvester.jpg')
earth=img.load()
cat=img2.load()



row=0
column=0


for row in range(600):
    for column in range(800):
        (r,g,b) = cat[column,row]
        if 130>r and g>150 and 130>b:
            cat[column,row] = earth[column,row]
        else:
            (re,ge,be)=earth[column,row]
            cat[column,row] = (int(4*r/5)-50+re,int(4*b/5)-50+ge,int(4*b/5)-50+be)


img2.show()
