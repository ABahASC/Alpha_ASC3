

board = [['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0']]
board[int(random(0,5))][int(random(0,5))] = 1
def setup():
    size(500,500)
    background(0)
    
def draw():
    global mx
    global my
    global board
    for i in range(len(board)):
        for j in range(len(board)):
            rect(i*100,j*100,100,100)
    if mousePressed:
        mx = int(mouseX/100)
        my = int(mouseY/100)
        if board[mx][my] == 1:
            print("You Win")
        elif board[mx][my] != 1:
            print("You Lose")
            
    
        
    