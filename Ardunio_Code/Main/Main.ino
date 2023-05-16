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
}

void loop() {
  // put your main code here, to run repeatedly:
  Temperature();
  Light();
  Moisture();
  //Serial.println(String(temp), " ", String(light), " ", String(moisture_voltage));
}
