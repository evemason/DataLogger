// including all libaries required

#include "Constants.h"
#include <Wire.h>

//include functions
extern void Temperature();
extern void Light();
extern void Moisture();
extern void Average(int sensor);
extern void info();
extern void convert();
extern void lightfeedback();

float temperatureC;

void setup() {
  // put your setup code here, to run once:
  // speed at which arduino passes data to the computor
  Serial.begin(9600);
  pinMode(LEDarray, OUTPUT);
  analogReference(DEFAULT);
}

void loop() {

  //Serial.println(light_voltage);
  if (Serial.available()>0){
    // read the imcoming byte 
    incomingByte = Serial.read();
    //Serial.println(incomingByte);
    n = 0;
    }

  if (incomingByte == 'T'){
    delay(200);

    Temperature();
    Average(temp_out);
    digitalWrite(led_temp, HIGH);
    digitalWrite(led_moisture, LOW);
    digitalWrite(led_light, LOW);
    if (n<20){
      Serial.println(String(temp_out));
      n = n+1;
    }
    else{
      Serial.println(String(av));
    }
  }
  if (incomingByte == 'L'){
    delay(200);

    Light();
    Average(light);
    digitalWrite(led_light, HIGH);
    digitalWrite(led_moisture, LOW);
    digitalWrite(led_temp, LOW);
    if (n<20){
      Serial.println(String(light));
      n = n+1;
    }
    else{
      Serial.println(String(av));
    }
    lightfeedback();
  }
  if (incomingByte == 'M'){
    delay(200);

    Moisture();
    Average(moisture);
    digitalWrite(led_moisture, HIGH);
    digitalWrite(led_light, LOW);
    digitalWrite(led_temp, LOW);
    if (n<20){
      Serial.println(String(moisture));
      n = n+1;
    }
    else{
      Serial.println(String(av));
    }
  }
  if (incomingByte == 'X'){
    digitalWrite(led_temp, LOW);
    digitalWrite(led_light, LOW);
    digitalWrite(led_moisture, LOW);
    }

  if (incomingByte == 'I'){
    info();
  }
}
