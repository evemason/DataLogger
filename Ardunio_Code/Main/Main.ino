// including all libaries required

#include "Constants.h"
#include <Wire.h>

//include functions
extern void Temperature();
extern void Light();
extern void Moisture();
extern void Average(int sensor);
extern void info();
extern void high_value();
extern void low_value();
extern void feedback(int value);

void setup() {
  // put your setup code here, to run once:
  // speed at which arduino passes data to the computor
  Serial.begin(9600);
  pinMode(Led, OUTPUT);
  analogReference(DEFAULT);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Temperature();
  //Light();
  //Average(light);
  //Moisture();
  //Serial.println(String(temp)+ "," + String(light) + "," +String(moisture_voltage));

  //temp_voltage = analogRead(temperature_pin);
  //Serial.println(temp);  
  
  //Serial.println(String(light_voltage) + "," + String(light_current)+  "," + String(light)+  "," + String(av));
  //Serial.println(av);
  //delay(1000); //collects data every second

  //Serial.println(String(av) + "computed average");
  //Serial.println("average 0 " + String(average[0]));
  //Serial.println("average 1 " + String(average[1]));
  //Serial.println("average 2 " + String(average[2]));
  
  //Serial.println(light_voltage);
  if (Serial.available()>0){
    // read the imcoming byte 
    incomingByte = Serial.read();
    //Serial.println(incomingByte);
    n = 0;
    }

  if (incomingByte == 'T'){
    delay(100);
    if (state != 0){
      state = 0;
      analogReference(INTERNAL);
    }
    Temperature();
    Average(temp);
    digitalWrite(led_temp, HIGH);
    digitalWrite(led_moisture, LOW);
    digitalWrite(led_light, LOW);
    if (n<20){
      Serial.println(String(temp));
      n = n+1;
    }
    else{
      Serial.println(String(av));
    }
    //delay(500);
  }
  if (incomingByte == 'L'){
    delay(100);
    if (state != 1){
      state = 1;
      analogReference(DEFAULT);
    }
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
  }
  if (incomingByte == 'M'){
    delay(100);
    if (state != 1){
      state = 1;
      analogReference(DEFAULT);
    }
    Moisture();
    Average(soilmoisturepercent);
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
    digitalWrite(led_feedback, LOW);
    digitalWrite(feedback_pin, LOW);
    }
  /*
  if (incomingByte == 'I'){
    digitalWrite(led_feedback, HIGH);
    //digitalWrite(feedback_pin, HIGH);
    //info();
    high_value();
  }
  if (incomingByte == 'a'){
    digitalWrite(led_feedback,LOW);
    low_value();
  }
  Light();
  feedback(light);*/
}
