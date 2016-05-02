import PIL.Image

image=Image.open("#IMAGEPATH#")
width=image.width
height=image.height
center_x=int(width/2)
center_y=int(height/2)
center=(center_x,center_y)
listData=list(image.getdata())
for i in range(len(listData)):
    px = i % ( width )
    py = math.trunc( i / width)
    x=px/width
    y=py/height
    pixel=listData[i]
    r=pixel[0]
    g=pixel[1]
    b=pixel[2]
    distance_center=sqrt(((px-center_x)**2)+((py-center_y)**2))
    #command#
image.putdata(listData)
image.save(self.workingImage)