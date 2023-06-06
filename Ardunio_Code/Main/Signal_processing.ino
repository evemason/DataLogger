void Temperature(){
  temp_voltage = analogRead(temperature_pin);
  R = (temp_voltage * R_const_temp)/(1023  - temp_voltage);

  float temp = 77.5*exp(-0.000182* R) - 6.7;

  //temp = - 3.03 * pow(10, -2) * R + 8.756;

  
  
  float temperature = analogRead(LM35);
  temperatureC = (temperature * 500/1024) - 273;

  temp_out = (temperatureC + temp)/2;
}

void Light(){
  light_voltage = analogRead(light_pin);
  //light_current = 1000000*5*light_voltage/(R_const_light*1023);
  //light = exp(log(light_current)-0.24);
  light = (1023 - light_voltage - 200)/1.5;
  if(light < 0){
    light = 0;
  }
}

void Moisture(){
  moisture_voltage = analogRead(moisture_pin);
  
  soilmoisturepercent = map(moisture_voltage, AirValue, WaterValue, 0, 100);
  if(soilmoisturepercent >= 100)
  {
    //Serial.println(moisture_voltage);
    //Serial.println("100 %");
    moisture = 100;
  }
  else if(soilmoisturepercent <=0)
  {
    //Serial.println(moisture_voltage);
    //Serial.println("0 %");
    moisture = 0;
  }
  else if(soilmoisturepercent >0 && soilmoisturepercent < 100)
  
  {
    //Serial.println(moisture_voltage);
    //Serial.print(soilmoisturepercent);
    //Serial.println("%");
    moisture = soilmoisturepercent;
}

}

void Average(unsigned long sensor){
  average[0] = average[1];
  average[1] = average[2];
  average[2] = sensor;
  av = (average[0]+average[1]+average[2])/lenght;
}
