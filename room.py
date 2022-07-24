from vpython import *
from time import *
mRadius = 0.75
wallThickness = 0.1
roomWidth = 15
roomDepth = 5
roomHeight = 10
floor = box(pos=vector(0,-roomHeight/2,0),color=color.white,size=vector(roomWidth,wallThickness,roomDepth))
ceiling = box(pos=vector(0,roomHeight/2,0),color=color.white,size=vector(roomWidth,wallThickness,roomDepth))
leftwall = box(pos=vector(-roomWidth/2,0,0),color=color.white,size=vector(wallThickness,roomHeight,roomDepth))
rightwall = box(pos=vector(roomWidth/2,0,0),color=color.white,size=vector(wallThickness,roomHeight,roomDepth))
backwall = box(pos=vector(0,0,-roomDepth/2),color=color.white,size=vector(roomWidth,roomHeight,wallThickness))
sphere1 = sphere(color=color.red,radius=mRadius)

deltaX=0.1
xPos=0
rightbounce = -roomWidth/2+wallThickness/2+mRadius
leftbounce = roomWidth/2-(wallThickness/2)-mRadius
while True:
	rate(40)
	xPos=xPos+deltaX
	if(xPos>leftbounce or xPos<rightbounce):
		deltaX=deltaX*(-1)
	sphere1.pos=vector(xPos,0,0)
