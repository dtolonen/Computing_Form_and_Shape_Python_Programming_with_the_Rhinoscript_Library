import rhinoscriptsyntax as rs

# Testing out teacher Carl's example no.2 and doing some code and manual tweaks.

surface = rs.GetObjects("pick surface", 8) # 8 Surface or single-face brep

rs.FlipSurface(surface) # Try this or manually flipping normals

uGrid= 20 # later 40
vGrid= 50 # later 120

uDomain = rs.SurfaceDomain(surface, 0) #domain direction 0 = U
vDomain = rs.SurfaceDomain(surface, 1) #domain direction 1 = V

uMin = uDomain[0]
uMax = uDomain[1]
vMin = vDomain[0]
vMax = vDomain[1]

uRange = uMax-uMin
vRange = vMax-vMin

uStep = uRange/uGrid # like units in the UV domain? 
vStep = vRange/vGrid # like units in the UV domain?

U = uMin
while U < uMax: # later (uMax*2):
	V = vMin
	while V<vMax:
		
		normal = rs.SurfaceNormal(surface, (U,V)) # note this function asks for a tuple while EvaluateSurface below takes separated U and V values.   
		scaledNormal = rs.VectorScale(normal, 15) # later 100
		pointOnSurface = rs.EvaluateSurface(surface, U,V)
		pointOffSurface = rs.VectorAdd(pointOnSurface, scaledNormal) # must check this out
		rs.AddLine(pointOnSurface,pointOffSurface)
		V=V+vStep
	U = U + uStep