// sensor results
extern const int temperature_pin = A0;
extern const int light_pin = A1;
extern const int moisture_pin = A2;
extern const int AirValue = 620;   //you need to replace this value with Value_1
extern const int WaterValue = 310;  //you need to replace this value with Value_2
extern const int led_light = 2;
extern const int led_moisture = 4;
extern const int led_temp = 3;


// Light output 
extern const int Led = 2;

// Restance values
extern int R_const_light = 220000;
extern int R_const_temp = 1000;

// processing constants
const int lenght = 3;
extern int light_voltage = 0, temp_voltage = 0, temp_R = 0, moisture_voltage = 0, temp = 0, det = 0, light = 0, light_current = 0, av =0, moisture=0;
extern int average[lenght] = {0,0,0};
extern int soilmoisturepercent=0;

// AnalogueReferene state 
extern int state = 0;

// Data array
extern char incomingByte='X'; // variable to store incoming data in
extern const byte numChars = 9;
extern char receivedChars[numChars]= {'X','X','X','X','X','X','X','X','X'};
extern int n = 0;
