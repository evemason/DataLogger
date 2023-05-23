import serial
import time
import tkinter as tk
from threading import Thread

reading_variable = False #global flag
idx = 0 #loop index
def off():
    ser.write(bytes('X', 'UTF-8'))
    global reading_variable
    reading_variable = False

sensor_data = []


def set_temp_sensor_button():
    ser.write(bytes('T', 'UTF-8'))
    global reading_variable
    reading_variable = True


def collect_data():
    global reading_variable
    if (reading_variable == True):
        print("hello")
        if (ser.in_waiting > 0):
            getData = ser.readline()
            dataString = getData.decode('utf-8')
            #print(dataString)
            sensor_data.append(dataString)
            print(sensor_data)

    window.after(100, collect_data)




ser = serial.Serial("COM4", 9600)
print("Reset Arduino")
#ser.write(bytes('X', 'UTF-8'))

window = tk.Tk()
window.geometry("300x200+200+100")
window.title("test reading and writing")

temp_button = tk.Button(window, text = "temperature", command = set_temp_sensor_button, height = 10, width = 10)
temp_button.pack()

off_button = tk.Button(window, text = "off", command = off, height = 10, width = 10)
off_button.pack()

window.after(1000, collect_data)

window.mainloop()

