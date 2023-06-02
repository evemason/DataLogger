#include <Wire.h>

char incomingByte = 'X';
int light = 2;
char x = 'X';

int count = 0;
int count0 = 0;
char lenh = 0;
char lenl = 0;

char recievedh2[2] = {'X','X'};
char recievedh3[3] = {'X','X','X'};
char recievedh4[4] = {'X','X','X','X'};

char recievedl2[2] = {'X','X'};
char recievedl3[3] = {'X','X','X'};
char recievedl4[4] = {'X','X','X','X'};

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
    appending();
  }
  
  else{
    digitalWrite(4,LOW); //blue low
    digitalWrite(2,LOW); //green low
    digitalWrite(3,LOW); // yellow 1 low
  }
    
}

void appending(){
  while(count0 < 1){ // Find the number of bytes that contain the high light level
    if(Serial.available()>0){
      incomingByte = Serial.read();
      lenh = incomingByte;
      count0 = count0 +1;
    }
  }
  count0 = 0;
  int h = lenh - '0';
  while(count < h){ //Store the high light level
    if(Serial.available()>0){
      incomingByte = Serial.read();
      if(lenh == '2'){
        recievedh2[count] = incomingByte;
      }
      if(lenh == '3'){
        recievedh3[count] = incomingByte;
      }
      if(lenh == '4'){
        recievedh4[count] = incomingByte;
      }
      count = count +1;
    }
  }
  count = 0;
  while(count0 < 1){ // Find the number of bytes for the low level
    if(Serial.available()>0){
      incomingByte = Serial.read();
      lenl = incomingByte;
      count0 = count0 +1;
    }
  }
  count = 0;
  int l = lenl - '0';
  while(count < l){ //Store the low light level
    if(Serial.available()>0){
      incomingByte = Serial.read();
      if(lenl == '2'){
        recievedl2[count] = incomingByte;
      }
      if(lenl == '3'){
        recievedl3[count] = incomingByte;
      }
      if(lenl == '4'){
        recievedl4[count] = incomingByte;
      }
      count = count +1;
    }
  }
  count0 = 0;
  if(lenh == '2'){ 
    if(recievedh2[0] == '4' && recievedh2[1] == '0'){
      digitalWrite(4,HIGH); //blue high
      digitalWrite(2,LOW); //green low
      digitalWrite(3,LOW); // yellow 1 low
    }
  }
  if(lenh == '3'){
    if(recievedh3[0] == '4' && recievedh3[1] == '0'&& recievedh3[2] == '0'){
      digitalWrite(4,LOW); //blue low
      digitalWrite(2,HIGH); //green high
      digitalWrite(3,LOW); // yellow 1 low
    }
  }
  if(lenh == '4'){  
    if(recievedh4[0] == '4' && recievedh4[1] == '0' && recievedh4[2] == '0' && recievedh4[3] == '0'){
      digitalWrite(4,HIGH); //blue high
      digitalWrite(2,HIGH); //green high
      digitalWrite(3,LOW); // yellow 1 low
    }
  }
  delay(3000);
  digitalWrite(4,LOW); //blue high
  digitalWrite(2,LOW); //green high
  digitalWrite(3,LOW); // yellow 1 low
  if(lenl == '2'){
    if(recievedl2[0] == '2' && recievedl2[1] == '0'){
      digitalWrite(4,LOW); //blue high
      digitalWrite(2,LOW); //green low
      digitalWrite(3,HIGH); // yellow 1 low
    }
  }
  if(lenl == '3'){  
    if(recievedl3[0] == '2' && recievedl3[1] == '0'&& recievedl3[2] == '0'){
      digitalWrite(4,HIGH); //blue low
      digitalWrite(2,LOW); //green high
      digitalWrite(3,HIGH); // yellow 1 low
    }
  }
  if(lenl == '4'){
    if(recievedl4[0] == '2' && recievedl4[1] == '0' && recievedl4[2] == '0' && recievedl4[3] == '0'){
      digitalWrite(4,LOW); //blue high
      digitalWrite(2,HIGH); //green high
      digitalWrite(3,HIGH); // yellow 1 low
    }
  }

  count = 0;
  delay(3000);
}
