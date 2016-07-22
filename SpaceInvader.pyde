from random import *
a=250
b=275
dir1= 10
x = 50
y = 0
step = 1
bullet = 430 
bulletX = 300
launch = False
aliens = [1,1,1,1]
lives=aliens.count(1)

def setup():
    size(500,500)
    noStroke()

def draw(): 
    global lives
    global aliens
    global launch
    global a
    global x
    global y
    global step
    global bullet
    global b
    background(255,255,255);
    global bulletX
    fill(255,0,0)
    for i in range(4):
        if aliens[i] == 1:            
            rect(i*100+x, y, 50, 50)
            if bullet < y and i*100+x <b + 14 < i*100+x+50:
                aliens[i] = 0
                lives=aliens.count(1)
                launch = False
                bullet = 430
        #bullet == "M"
    
    #fill(255,255,255)
    #rect(b + 14, bullet, 10, 10)
    if launch == True:
            fill(250,0,0)
            bullet = bullet - 5
            rect(bulletX, bullet, 10, 10)
    if bullet < 5:
        launch = False
        bullet = 430
    #if b + 14 == x:
    #    redraw
    #    fill(255)
    #    rect(x,y,50,50) 
    x+=step;
    if (x > width-350):
        x = width-350
        step = -1
    if (x < 0):
        x = 0
        y = y + 70
        step = 1
    if lives == 0:
        textSize(50)
        text("YOU WIN", 10, 50)
    if (y > 380):
        textSize(50)
        text("GAME OVER", 10, 100)
    fill(0,0,0)
    rect(b,440,50,10)    
    rect(a, 450, 100, 10)
    
def keyPressed():   
    global a
    global b
    global dir1
    global launch
    global bulletX
    bullet = 430 
    print("pressed key" , keyCode)
    if keyCode == 32:
        launch = True 
        bulletX = b + 14   
    if keyCode == 39:
        a=a+ dir1
    if keyCode == 37:
        a=a- dir1
    if keyCode == 39: #right arrow key
        b=b+ dir1
    if keyCode == 37: #left arrow key
        b=b- dir1

        
        