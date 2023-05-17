void Temperature(){
  temp_voltage = analogRead(temperature_pin);
  temp_R = ((5-temp_voltage)*R_const_temp)/(temp_voltage);
  det = pow(0.049,2) - 4*9.48*pow(10,-5)*(5.3-log(temp_R));
  temp = (0.049-pow(det,0.5))/(2*9.48*pow(10,-5));
}

void Light(){
  light_voltage = analogRead(light_pin);
  light_current = light_voltage/R_const_light;
  light = exp(log(light_current)+0.24);
}

void Moisture(){
  moisture_voltage = analogRead(moisture_pin);

}
