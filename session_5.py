
# Note 1 - for the general reader: this Python script is comprised of two phases. The first phase is currently active and you can run it in Rhino. Once the user has run the first phase to project their geometry and collected points onto an intermediary surface, they can COMMENT OUT the first phase code and run the second phase code to map those points onto the flat destination surface.   


# Note 2 - for Kadenze: programming this final exercise is still too challenging for my skills at the moment, SO MOST OF THE CODE WILL FOLLOW THE TEACHER CARL'S CODE in order to have some working code to see how it works with the Rhino model and learn about the structure of the code's logic. Still lacking in the coding skills, I will focus my efforts instead on experimenting on multiple destination surfaces. 
#
#  In the future, I hope I will learn from the code how to connect the two Python files and how to automatise this multiple surface projection. 
# 
# How: As the second phase is mostly a for loop, my hunch is that I could somehow change points = rs.getObjects to not let the user pick objects, but feed the points from the previous phase. I could also use the previously chosen referenceSurface and either let the user choose three designationSurfaces (how does one pause Python to let them choose objects later in the script?) or feed in object IDs (which would only work for this file and not other objects unless the IDs would change too). 
# 
# Then, I could perhaps wrap the whole rest of the code from the for loop downwards, in another for loop, which would loop through all the three items in destinationSurface...?  


import rhinoscriptsyntax as rs


# The First Phase - initial projection

curves = rs.ObjectsByType(4)
picturePlane = rs.GetObject("select the surface to use as the picture plane", 8)
eyePoint = rs.GetObject("select the point to use as the eye, the point at which the projected content will converge",1)


for curve in curves:
	pointsOnCurve = rs.DivideCurve(curve, 100)
	intersectionPoints = []
	closeCount = 0
	middleCount = 0
	farCount = 0
	for point in pointsOnCurve:
		
		if rs.Distance(point, eyePoint) < 80:
			layerName = "close"
			closeCount+=1
		elif rs.Distance(point, eyePoint) >= 80 and rs.Distance(point, eyePoint) <115:
			layerName = "middle"
			middleCount+=1
		else:
			layerName = "far"
			farCount+=1


		projector = rs.AddLine(point, eyePoint)
		
		rs.ObjectLayer(projector, layerName)

		intersections = rs.CurveSurfaceIntersection(projector, picturePlane)
		if intersections:
			intersectionPoint = intersections[0][1]
			pointObjectInSpace = rs.AddPoint(point) 

			rs.ObjectLayer(pointObjectInSpace, layerName)
			intersectionPoints.append(intersectionPoint)



	pointObs = rs.AddPoints(intersectionPoints)
	reconstructedCurve = rs.AddInterpCurve(intersectionPoints, 1) 

	if closeCount > middleCount and closeCount > farCount:
		rs.ObjectLayer(reconstructedCurve, "close")

	elif middleCount>farCount:
		rs.ObjectLayer(reconstructedCurve, "middle")

	else:
		rs.ObjectLayer(reconstructedCurve, "far")







# The Second Phase - mapping to a new flat, surface

points = rs.GetObjects("pick points to map",1)
referenceSurface = rs.GetObject("pick reference surface",8)
destinationSurface = rs.GetObject("pick destination surface",8) 

listOfDestinationPoints = []

for myPoint in points:

	UV = rs.SurfaceClosestPoint(referenceSurface, myPoint)
	
	U = UV[0]
	V = UV[1]
	


	domainUReferene= rs.SurfaceDomain (referenceSurface, 0)
	domainVReferene= rs.SurfaceDomain (referenceSurface, 1)

	rangeUReference = domainUReferene[1]-domainUReferene[0]
	rangeVReference = domainVReferene[1]-domainVReferene[0]

	relativeU = (U-domainUReferene[0]) / rangeUReference
	relativeV = (V-domainVReferene[0]) / rangeVReference


	
	domainUDestination = rs.SurfaceDomain(destinationSurface, 0)
	domainVDestination = rs.SurfaceDomain(destinationSurface, 1)
	
	rangeUDestination = domainUDestination[1]-domainUDestination[0]
	rangeVDestination = domainVDestination[1]-domainVDestination[0]


	absoluteU = relativeU * rangeUDestination + domainUDestination[0]
	absoluteV = relativeV * rangeVDestination + domainVDestination[0]


	pointOnDestination = rs.EvaluateSurface(destinationSurface, absoluteU, absoluteV)
	
	listOfDestinationPoints.append(pointOnDestination)
	rs.AddPoint(pointOnDestination)
	