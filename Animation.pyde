from random import *

def setup():
    size(400, 400)
    
def draw():
    rect(mouseX,mouseY, randrange(100), randrange(100))
    fill(randrange(255), randrange(255), randrange(255))