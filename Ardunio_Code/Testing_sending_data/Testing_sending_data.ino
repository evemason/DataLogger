#include <Wire.h>

char incomingByte = 'X';
int light = 2;
char x = 'X';

int count = 0;

char recieved[3] = {'X','X','X'};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(light, OUTPUT);
  
  

}

void loop() {
  if (Serial.available()>0){
    // read the imcoming byte 
    incomingByte = Serial.read();
    //Serial.println(incomingByte);
   
    }

  if (incomingByte == 'I'){
    
    //digitalWrite(2, HIGH); //green high
    //digitalWrite(4, LOW); //blue low
    //delay(100);
    appending();
  }
  else{
    digitalWrite(4,LOW); //blue low
    digitalWrite(2,LOW); //green low
    digitalWrite(3, LOW); // yellow 1 low
    digitalWrite(6,LOW); // yellow 2 High
    digitalWrite(5,HIGH); // red high
  }
    
}

void appending(){
  digitalWrite(5,LOW); //red Low
  while(count < 3){
    if(Serial.available()>0){
      //digitalWrite(6, HIGH); //yellow 2 high
      incomingByte = Serial.read();
      recieved[count] = incomingByte;
      count = count +1;
    }
  }
  if(count == 3){  
    digitalWrite(3,HIGH); // Yellow 1 HIgh
  }
  if(recieved[0] == '4'){
    digitalWrite(2,HIGH); //Green High
  }
  if(recieved[1] == '0'){
    digitalWrite(4,HIGH); // Blue High 
  }
  if(recieved[2] == '0'){
    digitalWrite(6,HIGH); // Yellow 2 High 
  }

  count = 0;
  delay(100);
}
