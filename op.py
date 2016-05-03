from PIL import Image
from math import *
#sys#

###########FUNCTIONS################3
def getPixelAt(px,py):
    global width, height,pixels
    i=int(((width*px)-1)+((height*py)-1))
    try:
        return pixels[i]
    except IndexError:
        return (0,0,0)
def getAverage(r,g,b):
    return int((r+g+b)/3)
def getAverageAsColor(color=(0,0,0)):
    global getAverage
    g=getGrayAverage(color[0],color[1],color[2])
    return (g,g,g)
def getLuma(r,g,b):
    return int(r* 0.3 + g* 0.59 + b * 0.11)
def getLumaAsColor(color=(0,0,0)):
    global getLuma
    l=getLuma(color[0],color[1],color[2])
    return (l,l,l)
def getDesaturated(r,g,b):
    return int( (max(r, g, b) + min(r, g, b) ) / 2)
def getDesaturatedAsColor(color=(0,0,0)):
    global getDesaturated
    d=getDesaturated(color[0],color[1],color[2])
    return (d,d,d)
def getGrayDecompositionMin(r,g,b):
    return min(r,g,b)
def getGrayDecompositionMax(r,g,b):
    return max(r,g,b)
def getGrayDecompositionMinAsColor(color=(0,0,0)):
    global getGrayDecompositionMin
    m=getGrayDecompositionMin(color[0],color[1],color[2])
    return (m,m,m)
def getGrayDecompositionMaxAsColor(color=(0,0,0)):
    global getGrayDecompositionMax
    m=getGrayDecompositionMax(color[0],color[1],color[2])
    return (m,m,m)
def getGrayQuant(r,g,b,n):
    f= 255 / (n - 1)
    av= (r + g + b) / 3
    g = int((av/ f) + 0.5) * f
    return g
def getGrayQuantAsColor(color=(0,0,0),n=3):
    global getGrayQuant
    g=getGrayQuant(color[0],color[1],color[2],n)
    return (g,g,g)

###########LOOP#############
def execute(fileName):
#TAB#file=fileName
#TAB#image=Image.open(file)
#TAB#width=image.width
#TAB#height=image.height
#TAB#center_x=int(width/2)
#TAB#center_y=int(height/2)
#TAB#center=(center_x,center_y)
#TAB#pixels=list(image.getdata())
#TAB#for i in range(len(pixels)):
#TAB#   px = i % ( width )
#TAB#   py = trunc( i / width)
#TAB#   x=px/width
#TAB#   y=py/height
#TAB#   color=pixels[i]
#TAB#   r=color[0]
#TAB#   g=color[1]
#TAB#   b=color[2]
#TAB#   distance_center=sqrt(((px-center_x)**2)+((py-center_y)**2))
#TAB#   distance_center_normX=distance_center/width
#TAB#   distance_center_normY=distance_center/height
#TAB#   vignet_factorX=1-distance_center_normX
#TAB#   vignet_factorY=1-distance_center_normY
#TAB#   #command#
#TAB#   pixels[i]=(int(r),int(g),int(b))
#TAB#image.putdata(pixels)
#TAB#image.save(file)

if __name__=="__main__":
    #if len(sys.argv)>1:
        execute(#IMAGEPATH#)
    #else: print("NO IMAGE")
