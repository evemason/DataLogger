We have made a plant care system to help novices grow plants. The system logs light, temperature and soil moisture level readings. Feedback has been implemented using the Arduino to control the light levels. 

To run the code:

1. upload the Arduino code located in the folder Arduino_Code titled Main
2. Run GUI.py this is located in the Interface_Code folder 
3. To run this 3 libraries need to be installed: Tkinter and PySerial and matplotlib


Features:

* Measure temperature, light and humidity. 
* Has 2 way commmunication between Arduino and Computer.
* Sends data to the computer every 300 ms. 
* Controls the light levels. 
* Linked to a database to provide tailored plant care recommendations based on specific plant types. 
* Ability to connect and monitor multiple plants using the same interface. 


Sensor farnell order codes:

* Phototransitor : 1497676
* Thermistor : 1187027
* Soil moisture level sensor : 2946124
* LM335 temperature sensor: 3124172
