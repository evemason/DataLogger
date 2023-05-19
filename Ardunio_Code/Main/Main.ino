// including all libaries required

#include "Constants.h"
#include <Wire.h>

//include functions
extern void Temperature();
extern void Light();
extern void Moisture();

void setup() {
  // put your setup code here, to run once:
  // speed at which arduino passes data to the computor
  Serial.begin(9600);
  pinMode(Led, OUTPUT);

  //analogReference(1);
}

void loop() {
  // put your main code here, to run repeatedly:
  Temperature();
  Light();
  //Moisture();
  //Serial.println(String(temp)+ "," + String(light) + "," +String(moisture_voltage));

  //light_voltage = analogRead(light_pin);
  //Serial.println(light_voltage);

  Serial.println(String(temp) + "," + String(light_current) + "," + String(light)+ "," + String(light_voltage));
}
