void info(){
  while(count0 < 1){ // Find the number of bytes that contain the high light level
    if(Serial.available()>0){
      incomingByte = Serial.read();
      lenh = incomingByte;
      count0 = count0 +1;
    }
  }
  count0 = 0;
  int h = lenh - '0';
  while(count < h){ //Store the high light level
    if(Serial.available()>0){
      incomingByte = Serial.read();
      if(lenh == '2'){
        recievedh2[count] = incomingByte;
      }
      if(lenh == '3'){
        recievedh3[count] = incomingByte;
      }
      if(lenh == '4'){
        recievedh4[count] = incomingByte;
      }
      count = count +1;
    }
  }
  count = 0;
  while(count0 < 1){ // Find the number of bytes for the low level
    if(Serial.available()>0){
      incomingByte = Serial.read();
      lenl = incomingByte;
      count0 = count0 +1;
    }
  }
  count = 0;
  int l = lenl - '0';
  while(count < l){ //Store the low light level
    if(Serial.available()>0){
      incomingByte = Serial.read();
      if(lenl == '2'){
        recievedl2[count] = incomingByte;
      }
      if(lenl == '3'){
        recievedl3[count] = incomingByte;
      }
      if(lenl == '4'){
        recievedl4[count] = incomingByte;
      }
      count = count +1;
    }
  }
  count0 = 0;
  count = 0;
  convert();
}

void convert(){
  if(lenl == '2'){
    int first = recievedl2[0] -'0';
    int second = recievedl2[1] - '0';
    low = first*10 + second;
  }
  if(lenl == '3'){
    int first = recievedl3[0] -'0';
    int second = recievedl3[1] - '0';
    int third = recievedl3[2] - '0';
    low = first*100 + second*10 + third;
  }
  if(lenl == '4'){
    int first = recievedl4[0] -'0';
    int second = recievedl4[1] - '0';
    int third = recievedl4[2] - '0';
    int fourth = recievedl4[3] - '0';
    low = first*1000 + second*100 + third*10 + fourth;
  }
  if(lenh == '2'){
    int first = recievedh2[0] -'0';
    int second = recievedh2[1] - '0';
    high = first*10 + second;
  }
  if(lenh == '3'){
    int first = recievedl3[0] -'0';
    int second = recievedl3[1] - '0';
    int third = recievedl3[2] - '0';
    high = first*100 + second*10 + third;
  }
  if(lenh == '4'){
    int first = recievedl4[0] -'0';
    int second = recievedl4[1] - '0';
    int third = recievedl4[2] - '0';
    int fourth = recievedl4[3] - '0';
    high = first*1000 + second*100 + third*10 + fourth;
  }
}

void lightfeedback(){
  lightaim = (high+low)/2
  outvoltage = lightaim - light
  if(outvoltage > 0){
    analogWrite(LEDarray,outvoltage);
  }
  else{
    analogWrite(LEDarray, 0);
  }
}
