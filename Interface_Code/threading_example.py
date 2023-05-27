import serial
import time
import tkinter as tk
from threading import Thread
from threading import *
import serial.tools.list_ports
import queue

global window
window = tk.Tk()
window.geometry("300x200+200+100")
window.title("test reading and writing")

q = queue.Queue()

# threading is a way to run code concurrently
# using queues to eliminate the need for global variables
# thread 1 : main thread - managing the GUI and program logic
# thread 2 : getting serial data
# thread 3: updating the GUI
global reading_variable
reading_variable = False #global flag


def off():
    ser.write(bytes('X', 'UTF-8'))
    global reading_variable
    reading_variable = False
    sensor_data.clear()

sensor_data = []


def set_temp_sensor_button():
    ser.write(bytes('T', 'UTF-8'))

    #display_box.delete("1.0", tk.END)
    #display_box.insert("1.0", sensor_data)

    global reading_variable
    reading_variable = True


def collect_data():
    global reading_variable, window
    #print(reading_variable)
    if (reading_variable == True):

        if (ser.in_waiting > 0):
            getData = ser.readline()
            dataString = int(getData.decode('utf-8'))
            #print(dataString)
            sensor_data.append(dataString)
            #print(sensor_data)
            q.put(dataString)

    window.after(100, collect_data)

data = []
def printing_data():
    while True:
        item = q.get()
        data.append(item)
        display_box.delete("1.0", tk.END)
        display_box.insert("1.0", data)
        print(item)
        q.task_done()


Thread1 = Thread(target = collect_data)
Thread1.start()

Thread2 = Thread(target = printing_data)
Thread2.start()

q.join()
ser = serial.Serial("COM4", 9600)
print("Reset Arduino")
#ser.write(bytes('X', 'UTF-8'))




temp_button = tk.Button(window, text = "temperature", command = set_temp_sensor_button, height = 1, width = 10)
temp_button.pack()

off_button = tk.Button(window, text = "off", command = off, height = 1, width = 10)
off_button.pack()

display_box = tk.Text(window, height = 20, width = 20)
display_box.pack()


window.mainloop()

