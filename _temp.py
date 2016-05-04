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

file='C:/Users/Juan/AppData/Local/TempWK_PhotoSafeLight.jpg'
image=Image.open(file)
width=image.width
height=image.height
center_x=int(width/2)
center_y=int(height/2)
center=(center_x,center_y)
pixels=list(image.getdata())
for i in range(len(pixels)):
   px = i % ( width )
   py = trunc( i / width)
   x=px/width
   y=py/height
   color=pixels[i]
   r=color[0]
   g=color[1]
   b=color[2]
   distance_center=sqrt(((px-center_x)**2)+((py-center_y)**2))
   distance_center_normX=distance_center/width
   distance_center_normY=distance_center/height
   vignet_factorX=1-distance_center_normX
   vignet_factorY=1-distance_center_normY
   
   z=0
   r=0
   w=1
   q=0
   g=0
   
   #command#
   pixels[i]=(int(r),int(g),int(b))
image.putdata(pixels)
image.save(file)

#if __name__=="__main__":
    #if len(sys.argv)>1:
        #execute('C:/Users/Juan/AppData/Local/TempWK_PhotoSafeLight.jpg')
    #else: print("NO IMAGE")
