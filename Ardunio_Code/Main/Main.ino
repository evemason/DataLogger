// including all libaries required

#include "Constants.h"
#include <Wire.h>

//include functions
extern void Temperature();
extern void Light();
extern void Moisture();
extern void Average(int sensor);
extern void info();

void setup() {
  // put your setup code here, to run once:
  // speed at which arduino passes data to the computor
  Serial.begin(9600);
  pinMode(Led, OUTPUT);
  analogReference(INTERNAL);
}

void loop() {
  // put your main code here, to run repeatedly:
  Temperature();
  //Light();
  Average(temp);
  //Moisture();
  //Serial.println(String(temp)+ "," + String(light) + "," +String(moisture_voltage));

  //temp_voltage = analogRead(temperature_pin);
  //Serial.println(temp);  
  
  //Serial.println(String(light_voltage) + "," + String(light_current)+  "," + String(light)+  "," + String(av));
  //Serial.println(av);
  //delay(1000); //collects data every second

  if (Serial.available()>0){
    // read the imcoming byte 
    incomingByte = Serial.read();
    }

  if (incomingByte == 'T'){
    if (state != 0){
      state = 0;
      analogReference(INTERNAL);
    }
    Temperature();
    Average(temp);
    Serial.println(String(av));
  }
  if (incomingByte == 'L'){
    if (state != 0){
      state = 0;
      analogReference(INTERNAL);
    }
    Light();
    Average(light);
    Serial.println(String(av));
  }
  if (incomingByte == 'M'){
    if (state != 1){
      state = 1;
      analogReference(DEFAULT);
    }
    Moisture();
    Average(soilmoisturepercent);
    Serial.println(String(av));
  }
  if (incomingByte == 'X'){}

  if (incomingByte == 'I'){
    info();
  }
  else{
    Serial.println("lost data");
  }
}
