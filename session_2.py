


import rhinoscriptsyntax as rs 
import random, math


def main_curve(y):
	listOfPoints=[]
	for x in range(0,90,20):
		z = (x/5)*math.sin(x/50)+20*math.sin(x+y/20)
		if x == 75:
			z+= random.uniform(-20,35)
			x+= random.uniform(-20,35)
		listOfPoints.append((x-50,y-100,z)) # later corrections x- and y- to fit in 100 box

	rs.AddCurve(listOfPoints,3) 

def large_blip_curve(y):
	listOfPoints=[]
	for x in range(0,100,10):
		z = (x/5)*math.tan(x/10)+10*math.cos(x+y/20)
		
		z+= random.uniform(30,30)
		x+= random.uniform(30,30)
		listOfPoints.append((x-50,y-100,z)) # later corrections x- and y- to fit in 100 box

	rs.AddInterpCurve(listOfPoints,3)



for curves in range(0,200,3):
	draw_curve = main_curve(curves)
	if curves > 70:
		large_blip_curve(curves)
	else:
		main_curve(curves)

