x=200;
y=1;
speed = 1

def setup():
  size (400,400);
  smooth();
  background(0);
  noStroke();
  fill(0,255,0);
def draw():
    global x
    global y
    global speed
    background(0);
    rect(mouseX,330,40,40)
    ellipse(x, 200, 40, 40);
    x=x+y;
    if (x>width-20 or x<20):
        y=-y;
        
        