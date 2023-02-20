import rhinoscriptsyntax as rs 
import random

# Testing some of Carl the teacher's simpler snippets to get a hang of all of this and, then, while running one or the other snippets, adjusting the Rhino model manually. 

pickedCurves = rs.GetObjects("pick some curves", 4)


# 1st Run

# for curve in pickedCurves:
# 	startPoint = rs.CurveMidPoint(curve)
# 	goalPoint = (startPoint[0], startPoint[1], 0)
# 	pathLine = rs.AddLine(goalPoint, startPoint) 
	

# 	rs.ExtrudeCurve(curve, pathLine) # see what reversing these does
# 	rs.DeleteObject(pathLine)
	
# 2nd Run

if len(pickedCurves) < 5:
	print ("you must pick at least two curves")
else:
	random.shuffle(pickedCurves)
	rs.AddLoftSrf(pickedCurves)

rs.AddLoftSrf(pickedCurves)
