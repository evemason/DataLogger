import serial
import time
import tkinter as tk

def off():
    ser.write(bytes('X', 'UTF-8'))

sensor_data = []

b = 0
def set_temp_sensor_button():
    ser.write(bytes('T', 'UTF-8'))
    global b
    b += 1
    #sensor_data = []
    while (b%2 == 0):
        getData = ser.readline()
        dataString = getData.decode('utf-8')
        print(dataString)
        sensor_data.append(int(dataString))
        print(sensor_data)

ser = serial.Serial("COM4", 9600)
print("Reset Arduino")
ser.write(bytes('X', 'UTF-8'))

window = tk.Tk()
window.geometry("300x200+200+100")
window.title("test reading and writing")

temp_button = tk.Button(window, text = "temperature", command = set_temp_sensor_button, height = 10, width = 10)
temp_button.pack()

off_button = tk.Button(window, text = "off", command = off, height = 10, width = 10)
off_button.pack()

window.mainloop()

