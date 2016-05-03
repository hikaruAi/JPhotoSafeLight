from PIL import Image
from math import *
import numpy

image=Image.open("#IMAGEPATH#")
width=image.width
height=image.height
center_x=int(width/2)
center_y=int(height/2)
center=(center_x,center_y)
pixels=numpy.asarray(image)
pixels.flags.writeable=True
maxx=len(pixels)
maxy=len(pixels[0])
for px in range(maxx):
    for py in range(maxy):
        x=px/width
        y=py/height
        color=pixels[px,py]
        r=color[0]
        g=color[1]
        b=color[2]
        distance_center=sqrt(((px-center_x)**2)+((py-center_y)**2))
        #command#
        pixels[px,py]=(int(r),int(g),int(b))
image=Image.fromarray(numpy.uint8(pixels))
image.save(self.workingImage)


def getPixelAt(px,py):
    return pixels[px,py]