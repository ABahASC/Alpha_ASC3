from Myro import *
from Graphics import *
from random import *

width = 500
height = 500
sim = Simulation("Maze World", width, height, Color("gray"))

#outside walls
sim.addWall((10, 10), (490, 20), Color("black"))
sim.addWall((10, 10), (20, 490), Color("black"))
sim.addWall((480, 10), (490, 490), Color("black"))
sim.addWall((10, 480), (490, 490), Color("black"))

#blue spot
poly = Circle((50, 50), 45)
poly.bodyType = "static"
poly.color = Color("red")
poly.outline = Color("black")
sim.addShape(poly)

#red spot
poly = Circle((450, 50), 45)
poly.bodyType = "static"
poly.color = Color("blue")
poly.outline = Color("black")
sim.addShape(poly)

#green spot
poly = Circle((50, 450), 45)
poly.bodyType = "static"
poly.color = Color("green")
poly.outline = Color("black")
sim.addShape(poly)

#yellow spot
poly = Circle((450, 450), 45)
poly.bodyType = "static"
poly.color = Color("yellow")
poly.outline = Color("black")
sim.addShape(poly)

#begin simulation and sets robot's position
makeRobot("SimScribbler", sim)
sim.setPose(0, width/2, height/2, 0)

sim.setup()

# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW

#The following is a helper function 
#Inputs: A picture and a color represented by the list above
#Returns the average x location of the color in the picture or -1 if the robot has found the color spot

def findColorSpot(picture, color):
    xPixelSum = 0
    totalPixelNum = 0
    averageXPixel = 0

    show(picture)

    for pixel in getPixels(picture):
        if(color == 1 and getRed(pixel) > 200 and getGreen(pixel) == 0 and getBlue(pixel) == 0):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 2 and getRed(pixel)== 0 and getGreen(pixel) > 90 and getBlue(pixel) == 0):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 3 and getRed(pixel) == 0 and getGreen(pixel) == 0 and getBlue(pixel) > 200):
          
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 4 and getRed(pixel) > 180 and getGreen(pixel) > 180 and getBlue(pixel) == 0):
            
            xPixelSum += getX(pixel)
            totalPixelNum += 1
    if(totalPixelNum != 0):
        averageXPixel = xPixelSum/totalPixelNum

    #Handles the case where robot has found the spot if it is near it
    #If necessary adjust the value
    if(totalPixelNum/(getWidth(picture)*getHeight(picture)) > 0.21):
        averageXPixel = -1

    return averageXPixel


# Use the following integers for colors:
# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW
# 5-BLACK
######################Code Starts Here##################################
x = int(input("Enter an integer: "))
penDown()
picture = takePicture()
value = findColorSpot(picture, x)
takePicture()
picture = takePicture()
value = findColorSpot(picture, x)
while value is findColorSpot(picture, x):
  if value != 1:
    takePicture()
    show(takePicture())
    turnBy(45, "deg")
    picture = takePicture()
    value = findColorSpot(picture, x)
    print(value)
  if value > 0:
    forward(1, 5)
takePicture()
show(takePicture())
backward(1, 5)

value2 = findColorSpot(picture, 2)
while value2 is findColorSpot(picture, 2):
  if value2 != 1:
    takePicture()
    show(takePicture())
    turnBy(45, "deg")
    picture = takePicture()
    value2 = findColorSpot(picture, 2)
    print(value2)
  if value2 > 0:
    forward(1, 5)
takePicture()
show(takePicture())
backward(1, 5)

value3 = findColorSpot(picture, 3)
while value3 is findColorSpot(picture, 3):
  if value3 != 1:
    takePicture()
    show(takePicture())
    turnBy(45, "deg")
    picture = takePicture()
    value3 = findColorSpot(picture, 3)
    print(value3)
  if value3 > 0:
    forward(1, 5)
takePicture()
show(takePicture())
backward(1, 5)

value4 = findColorSpot(picture, 4)
while value4 is findColorSpot(picture, 4):
  if value4 != 1:
    takePicture()
    show(takePicture())
    turnBy(45, "deg")
    picture = takePicture()
    value4 = findColorSpot(picture, 4)
    print(value4)
  if value4 > 0:
    forward(1, 5)
takePicture()
show(takePicture())
backward(1, 5)
penDown()
turnBy(90)
forward (1, 1)
turnBy(45)
forward(1, 1)
backward(1, 1)
turnBy (270)
forward (1, 1)
turnBy(-137)
forward(1, 2)
backward(1, 2)
turnBy(45)
forward(1, 1)
turnBy(90)
forward(1, 1)
turnBy(-135)
forward(1, 2)
motors(-1, 2, 5)
turnBy(330)
motors(2, -1, 4.4)
turnBy(90)
