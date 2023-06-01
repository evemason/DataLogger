#include <Wire.h>

char incomingByte = 'X';
int light = 2;
char x = 'X';

int count = 0;

char recieved[4] = {'X','X','X','X'};

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
    
    digitalWrite(2, HIGH); //green high
    digitalWrite(4, LOW); //blue low
    //delay(100);
    appending();
  }
    else{
      digitalWrite(4,HIGH); //blue high
      digitalWrite(2,LOW); //green low
    }
    
}

void appending(){
  digitalWrite(3, HIGH); //yellow 1 high
  while(count < 3){
    if(Serial.available()>0){
      digitalWrite(6, HIGH); //yellow 2 high
      count = count +1;
      x = Serial.read();
    }
    
    
  }
  if(count == 3){
    delay(100);
    digitalWrite(3, LOW); //yellow 1 low 
    
  }

  count = 0;
}
