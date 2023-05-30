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
  //Average(temp);
  //Moisture();
  //Serial.println(String(temp)+ "," + String(light) + "," +String(moisture_voltage));

  //temp_voltage = analogRead(temperature_pin);
  //Serial.println(temp);  
  
  //Serial.println(String(light_voltage) + "," + String(light_current)+  "," + String(light)+  "," + String(av));
  //Serial.println(av);
  //delay(1000); //collects data every second

  //Serial.println(String(av));
  
  Serial.println(temp);
  if (Serial.available()>0){
    // read the imcoming byte 
    incomingByte = Serial.read();
    //Serial.println(incomingByte);
    n = 0;
    }

  if (incomingByte == 'T'){
    if (state != 0){
      state = 0;
      analogReference(INTERNAL);
    }
    Temperature();
    Average(temp);
    digitalWrite(led_temp, HIGH);
    digitalWrite(led_moisture, LOW);
    digitalWrite(led_light, LOW);
    if (n<3){
      Serial.println(String(temp));
    }
    else{
      Serial.println(String(av));
    }
    //delay(500);
  }
  if (incomingByte == 'L'){
    if (state != 0){
      state = 0;
      analogReference(INTERNAL);
    }
    Light();
    Average(light);
    digitalWrite(led_light, HIGH);
    digitalWrite(led_moisture, LOW);
    digitalWrite(led_temp, LOW);
    if (n<3){
      Serial.println(String(light));
    }
    else{
      Serial.println(String(av));
    }
  }
  if (incomingByte == 'M'){
    if (state != 1){
      state = 1;
      analogReference(DEFAULT);
    }
    Moisture();
    Average(soilmoisturepercent);
    digitalWrite(led_moisture, HIGH);
    digitalWrite(led_light, LOW);
    digitalWrite(led_temp, LOW);
    if (n<3){
      Serial.println(String(moisture));
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
