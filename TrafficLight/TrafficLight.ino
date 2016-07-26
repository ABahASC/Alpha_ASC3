/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the Uno and
  Leonardo, it is attached to digital pin 13. If you're unsure what
  pin the on-board LED is connected to on your Arduino model, check
  the documentation at http://www.arduino.cc

  This example code is in the public domain.

  modified 8 May 2014
  Program discription: Basic traffic light arduino thing 
  Date: 7/26/2016
  Authors:  Kid Moko, Yung Adonis, Alpha
  by Scott Fitzgerald -- Sike  
 */


int RedLED = 12 ;
int YellowLED = 11;
int GreenLED = 10;
int Red2LEd = 8;
int Green2LED = 9;
int buttonState;
int buttonPin = 3;
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 13 as an output.
  pinMode(RedLED, OUTPUT);
  pinMode(YellowLED,OUTPUT);
  pinMode(GreenLED,OUTPUT);

}

// the loop function runs over and over again forever
void loop() {
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed.
  // if it is, the buttonState is HIGH:
  if (buttonState == HIGH){
      digitalWrite(GreenLED, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(1000);              // wait for a second
      digitalWrite(GreenLED, LOW);    // turn the LED off by making the voltage LOW
      delay(1000);              // wait for a second
      digitalWrite(YellowLED,HIGH);
      delay(1000);
      digitalWrite(YellowLED,LOW);
      delay(1000);
      digitalWrite(RedLED,HIGH);
      delay(1000);
      digitalWrite(RedLED,LOW);
      delay(1000);
  } else {
    // turn LED off:
    digitalWrite(GreenLED, HIGH);
  }

}
