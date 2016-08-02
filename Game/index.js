var img;
var x = 350;
var y = 700;
var speed = 3;
var myX=1;
var myY=1;
var points = 0;
var xD=0;
var yD=0;
//all variables
function preload(){
  img = loadImage("https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Soccer_ball.svg/2000px-Soccer_ball.svg.png");
  
}
function countPixels(array, value){
    var count = 0;
    for (var i=0; i < array.length; i++){
            if (array[i] == value){
                count +=1;
            }
        }
        return count;
    }
function makeLevel() {
  background(0,255,0);
  fill(0);
  rect(0,760,900,50);
  fill(255, 0, 0);
  ellipse(x, y, 50, 50);
}
//bounce function
function bounce() {
  points+=1;
  $("p").text(points);
  if (points%5==0){
    speed+=1;
  }
  if (myX > width/2){
    xD=1;
  }
  else{
    xD=0;
  }
  if (myY > height/2){
    yD=1;
  }
  else{
    yD=0;
  }
}
function setup() {
  createCanvas(530, 800);
  makeLevel();
  $("canvas").css({"margin-right":"auto", "margin-left":"auto","display":"block"});
  img.resize(60,0);
  imageMode(CENTER)
  loadPixels();//take snapshot of current canvas
  totalGoal = countPixels(pixels, 0);
  totalPlayer = countPixels(pixels, 255);
}
function draw() {
    //the soccer field
  makeLevel();
  background(0,255,0);
  fill(0,0,0);
  rect(1,760,900,50);
  if (keyIsDown(LEFT_ARROW))
    x-=5;

  if (keyIsDown(RIGHT_ARROW))
    x+=5;
        //player
  fill(255, 0, 0);
  ellipse(x, y, 50, 50);
  //the ball movement
  if (yD>.5){
    myY+=speed;
    if (myY>=height-img.height/2){
      yD=0;
    }
  }
  else{
    myY-=speed;
    if (myY<=0+img.height/2){
      yD=1;
    }
  }

  if (xD>.5){
    myX+=speed;
    if (myX>=width-img.width/2){
      xD=0;
    }
  }
  else{
    myX-=speed;
    if (myX<=0+img.width/2){
      xD=1;
    }
  }
  image(img, myX, myY);
  if (myY > 750) {
    myX=1;
    myY=1;
  }
  loadPixels();
  if(countPixels(pixels, 0) < totalGoal) {
  }

  else if(countPixels(pixels, 255) < totalPlayer){
  }

}