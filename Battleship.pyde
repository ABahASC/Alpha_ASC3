turns=0
board = [["0", "0", '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0']]
board[int(random(0,5))][int(random(0,5))] = "1"
def setup():
    size(500,500)
    background(0)
    img = loadImage("CarltonDance.gif")

def draw():
    global img
    global turns
    global board
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "0" or board[i][j] == "1":
                fill(255,255,255)
                rect(i*100,j*100,100,100)
            elif board[i][j] == "H":
                fill(0,0,0)
                rect(i*100,j*100,100,100)
                img = loadImage("CarltonDance.gif")
                image(img, 0, 0)
                image(img, 0, 0, 0,0)
                background(255);  
                fill(0);
                textSize(80)
                text("YOU WIN",100,100)
                print(board[i][j])
            else:
                fill(255,255,0)
                rect(i*100,j*100,100,100)
def mousePressed():
    global turns
    mx = int(mouseX/100)
    my = int(mouseY/100) 
    if board[mx][my] == "1":
        print("You Win")
        board[mx][my] = "H"
        textSize(50)
        text("YOU WON",255,0,0) 
        print("you win")
    elif board[mx][my] == "0":
        board[mx][my] = "M"
        print("you missed)

    if turns>4:
        background(255);  
        fill(0);
        textAlign(CENTER,CENTER);
        text("GAME OVER",width/2,height/2)

    
    