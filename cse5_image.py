from PIL import Image, ImageDraw
# prepare an image and its drawing context
img=Image.new('RGB', (120,90))
context=ImageDraw.Draw(img)

# draw robot's mouth, nose, and eyes
context.rectangle([10,50,110,80], fill='blue', outline='blue')
context.rectangle([50,35,70,55], fill='blue', outline='blue')
context.rectangle([15,10,45,30], fill='red', outline='yellow')
context.rectangle([75,10,105,30], fill='red', outline='yellow')

# display the result
img.show()