#!/bin/python3

import sys
from PIL import Image, ImageDraw, ImageFont

# Get the name input passed
# if len(sys.argv) > 2:
#     nObra = sys.argv[1]
#     nAutor = sys.argv[2]

nObra = "Calling of\nSt. Matthew"
nAutor = 'Michelangelo Merisi da Caravaggio'
font = "data/font/Pirata_One/PirataOne-Regular.ttf"
imageDir = "data/calling-of-saint-matthew.jpeg"
color = 'rgb(255, 255, 255)'


# create Image object with the input image
image = Image.open(imageDir)

# Get the size of the image
w, h = image.size

# initialise the drawing context with
# the image object as background
draw = ImageDraw.Draw(image)

# create font object with the font file and specify
# desired size
fonte_obra = ImageFont.truetype(font, size=600)
fonte_autor = ImageFont.truetype(font, size=150)

# Get the size of the message
obra_w, obra_h = draw.textsize(nObra, fonte_obra)

# draw the message on the background
draw.multiline_text((w/2 - obra_w/2 ,h/2 - obra_h/2), nObra, fill=color, font=fonte_obra, align='center')

# Get the size of the message
autor_w, autor_h = draw.textsize(nAutor, fonte_autor)

# draw the message on the background
draw.text((w/2 - autor_w/2, h/2 + obra_h/2), nAutor, fill=color, font=fonte_autor)

# save the edited image
image.save("New_" + imageDir.split('/')[-1])

#loadImage
image.show()
