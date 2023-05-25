void Temperature(){
  temp_voltage = analogRead(temperature_pin);
  temp_R = (R_const_temp*1.1*temp_voltage)/(5*1023-temp_voltage*1.1);
  //det = 0.049 * 0.049 - 4 * 0.0000948 * (5.3 - log(temp_R));
  //det = pow(0.049,2) - 4*9.48*pow(10,-5)*(5.3-log(temp_R));
  //temp = (0.049-pow(det,0.5))/(2*9.48*pow(10,-5));
  //temp = (0.049 - sqrt(det))/(2*0.0000948);
  temp = (5.36-log(temp_R))/(0.0481);
}

void Light(){
  light_voltage = analogRead(light_pin);
  light_current = 1000000*1.1*light_voltage/(R_const_light*1023);
  light = exp(log(light_current)-0.24);
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

void Average(int sensor){
  average[0] = average[1];
  average[1] = average[2];
  average[2] = sensor;
  av = (average[0]+average[1]+average[2])/lenght;
}

void info() {
    static byte ndx = 0;
    char endMarker = '\n';
    
    while (incomingByte != 'L') {
        incomingByte = Serial.read();

        if (imcomingByte != endMarker) {
            receivedChars[ndx] = imcomingByte;
            ndx++;
            if (ndx >= numChars) {
                ndx = numChars - 1;
            }
        }
        else {
            receivedChars[ndx] = '\0'; // terminate the string
            ndx = 0;
        }
    }
}
