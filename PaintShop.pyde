from random import *

pick = 0

def setup():
    size (400, 400)
    
def mouseDragged():
    ellipse(mouseX, mouseY, 10, 10)
    
def draw():
    global pick 
    
    strokeWeight(.1)
    fill(255,0,0)
    rect(0,0,100,100)
    fill(0,255,0)
    rect(100,0,100,100)
    fill(0,0,255)
    rect(200,0,100,100)
    fill(randrange(225),randrange(100),0)
    rect(300,0,100,100)
    
    if mouseButton == LEFT:
        if mouseY < 100:
            if mouseX < 100:
                pick = 1
                fill(255, 0, 0)
                mouseDragged()
            if 100<mouseX<200:
                pick = 2
            if 200<mouseX<300:
                pick = 3
            if 300<mouseX<400:
                pick = 4 
                
        if mouseY > 100:
            if pick == 1:
                fill(255, 0, 0)
            if pick == 2:
                fill(0, 255, 0)
            if pick == 3:
                fill(0,0,255)
            if pick == 4:
                fill(randrange(255),randrange(255),randrange(255))
            mouseDragged()
            
    elif mouseX>100:
        pick = 1
        fill(255,0,0)
    elif mouseX>200:
        pick = 2
        fill(0,255,0)
    elif mouseX>300:
        pick = 3
        fill(0,0,255)
    elif mouseY>400:
        pick = 3
        fill(0,0,255)

    
    
    
            
   
        stroke(mouseX, mouseY,10,10)
        ellipse(mouseX,mouseY,randrange(10),randrange(10))
    if mouseY < 100:
        fill (255,0,0)
        ellipse (mouseX,mouseY, 30, 40)