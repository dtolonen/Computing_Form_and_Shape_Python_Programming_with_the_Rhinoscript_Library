import rhinoscriptsyntax as rs 
import random

count = 0
while count < 500000: 
    x = random.uniform(-100,100) # keep all points within a -100 to 100 cube
    y = random.uniform(-100,100)
    z = random.uniform(-100,100)
    point = (x,y,z)


# RUN 1 - note: comment out all but one run if you wish to separate the runs on different Rhino layers

larger shape
    if rs.Distance(point, (0,0,0)) > 80 and rs.Distance(point, (0,0,0)) < 95:
        if (x > -20 and x < 100 and y > -100 and y < 50 and z > -50 and z < 90) and not (x > -30 and x < 100 and z > -20 and z<40):
            rs.AddPoint(point)

#lower small shape
    if rs.Distance(point, (-20,-10,0)) > 20 and rs.Distance(point, (-20,-10,0)) < 35:
        if (x > -90 and x < 25 and y > -15 and y < 5 and z > 0 and z < 70) and not (x > -10 and x < 25 and y > -75 and y < 5 and z > -40 and z<10):
            if z < 0:
                z = 0
            rs.AddPoint(point)


higher small shape
    if rs.Distance(point, (-80,0,50)) > 20 and rs.Distance(point, (-80,0,50)) < 35:
        if (x > -90 and x < 25 and y > -15 and y < 5 and z > 0 and z < 70) and not (x > -10 and x < 25 and y > -75 and y < 5 and z > -40 and z<10):
            
            rs.AddPoint(point)


# RUN 2
larger shape
    if rs.Distance(point, (0,0,0)) > 80 and rs.Distance(point, (0,0,0)) < 95:
        if (x > -20 and x < 100 and y > -100 and y < 50 and z > -50 and z < 90) and not (x > -30 and x < 100 and z > -10 and z<10):
            rs.AddPoint(point)

#lower small shape
    if rs.Distance(point, (-20,-10,0)) > 20 and rs.Distance(point, (-20,-10,0)) < 35:
        if (x > -90 and x < 25 and y > -15 and y < 5 and z > 0 and z < 70) and not (x > -10 and x < 5 and y > -75 and y < 5 and z > -10 and z<10):

            rs.AddPoint(point)

# RUN 3

larger shape
    if rs.Distance(point, (0,0,0)) > 40 and rs.Distance(point, (0,0,0)) < 75:
        if (x > -20 and x < 70 and y > -70 and y < 30 and z > -30 and z < 50) and not (x > -30 and x < 70 and z > -40 and z<40):
            rs.AddPoint(point)

#lower small shape
    if rs.Distance(point, (-20,-10,0)) > 10 and rs.Distance(point, (-20,-10,0)) < 35:
        if (x > -90 and x < 25 and y > -15 and y < 5 and z > 0 and z < 70) and not (x > -10 and x < 5 and y > -45 and y < 5 and z > -10 and z<10):
            
            rs.AddPoint(point)



# RUN 4

larger shape
    if rs.Distance(point, (0,60,0)) > 40 and rs.Distance(point, (0,60,0)) < 75:
        if (x > -20 and x < 10 and y > -70 and y < 30 and z > -30 and z < 50):
            rs.AddPoint(point)

# RUN 5


#lower small shape
    if rs.Distance(point, (-9,-19,19)) > 10 and rs.Distance(point, (-19,-19,9)) < 35:
        if (x > -55 and x < 75 and y > -55 and y < 5 and z > 0 and z < 70) and not (x > -10 and x < 5 or y > -15 and y < 5 and z > -10 and z<10):
            
            rs.AddPoint(point)




    count += 1