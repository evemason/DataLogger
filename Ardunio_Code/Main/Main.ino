// including all libaries required

#include "Constants.h"
#include <Wire.h>

//include functions
extern void Temperature();
extern void Light();
extern void Moisture();
extern void Average(int sensor);



void setup() {
  // put your setup code here, to run once:
  // speed at which arduino passes data to the computor
  Serial.begin(9600);
  pinMode(Led, OUTPUT);

  //analogReference(INTERNAL);
}

void loop() {
  // put your main code here, to run repeatedly:
  Temperature();
  Light();
  Average(light);
  Moisture();
  //Serial.println(String(temp)+ "," + String(light) + "," +String(moisture_voltage));

  //temp_voltage = analogRead(temperature_pin);
  //Serial.println(temp);  
  
  //Serial.println(String(light_voltage) + "," + String(light_current)+  "," + String(light)+  "," + String(av));
}
