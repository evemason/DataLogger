void info() {
    static byte ndx = 0;
    char endMarker = '\n';
    
    while (incomingByte != 'L') {
        incomingByte = Serial.read();

        if (incomingByte != endMarker) {
            receivedChars[ndx] = incomingByte;
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

void high_value(){
  int i;
  //digitalWrite(feedback_pin, HIGH);
  while(incomingByte != 'a'){
    digitalWrite(feedback_pin, HIGH);
    incomingByte = Serial.read();
    if(incomingByte =='a'){
      digitalWrite(feedback_pin, LOW);
      break;
    }
    else{
      //want to append the incoming bytes to an array 
      recieved_high[i] = incomingByte;
      i++;
    }
  }
  high = int(recieved_high[0])*100 + int(recieved_high[1])*10 + int(recieved_high[2]);
}

void low_value(){
  int i;
  while(incomingByte != 'L'){
    incomingByte = Serial.read();
    if(incomingByte =='L'){
      break;
    }
    else{
      //want to append the incoming bytes to an array 
      recieved_low[i] = incomingByte;
      i++;
    }
  }

  low = int(recieved_low[0])*100 + int(recieved_low[1])*10 + int(recieved_low[2]);
}

void feedback(int light_value){
  if (light_value < low){
    digitalWrite(feedback_pin,HIGH);
  }
  else if (light_value > high){
    digitalWrite(feedback_pin, LOW);
  }
}


void bytes_high(){
  for (int i, i<2, i++){
    x = Serial.read();
    recieved_high[i] = x;
  }
}
