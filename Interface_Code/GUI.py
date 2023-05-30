from tkinter import *
import tkinter as tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from tkinter import ttk
import serial.tools.list_ports
import serial
import time
import tkinter as tk
import numpy as np
from threading import Thread
import queue
from Databaseclass import Database
import gc ## this might solve the problem but i am not sure how. 

# Global variables
s = False
reading_variable = False
gwater_level_high = Database.water_level_high('Tropical')
gwater_level_low = Database.water_level_low('Tropical')
gtemp_level_high = Database.temp_level_high('Tropical')
gtemp_level_low = Database.temp_level_low('Tropical')
glight_level_high = Database.light_level_high('Tropical')
glight_level_low = Database.light_level_low('Tropical')
high = 0
low = 0
sensor_data = []
new_data = 0 
sensor_type = 'off'


colour_light = "palegreen3"
colour_dark = "palegreen4"

Categories = ["Tropical", "Cactus", "Alpine", "Bulbs", "Climbers", "Ferns"]

window = Tk()

window.title("Plant Care System")
window.configure(bg=colour_light)

# create queues for the sensor values
q = queue.Queue()


width = 800
height = 600
XPOS = 350
YPOS = 100

text = str(width) + "x" + str(height) + "+" + str(XPOS) + "+" + str(YPOS)

data = pd.read_csv(r'Database\Plant_data.csv')

#print(data)
Categories = ["Tropical", "Cactus", "Alpine", "Bulbs", "Climbers", "Ferns"]


def entry_update(name):
    global gwater_level_high, gwater_level_low, gtemp_level_high, gtemp_level_low, glight_level_high, glight_level_low
    gwater_level_high, gwater_level_low, gtemp_level_high, gtemp_level_low, glight_level_high, glight_level_low = Database.extract_all(name)
    global sensor_type, high, low 
    if sensor_type == 'Light':
        high = glight_level_high
        low = glight_level_low
    if sensor_type == 'Temperature':
        high = gtemp_level_high
        low = gtemp_level_low
    if sensor_type == 'Moisture':
        high = gwater_level_high
        low = gwater_level_low
    text = Database.extract_all(name)
    entry.delete("1.0", tk.END)
    entry.insert("1.0", text)


entry = Text(window, bd=0, width=25, height=22)
entry.place(x=550, y=220)

recommendations = Label(window, text="Plant care recommendations", bg=colour_dark, fg="white", width=28)
recommendations.place(x=550, y=200)

button_dict = {}


# create a function which is called when a sensor button is clicked
def graph_update(type):
    global s
    global gwater_level_high, gwater_level_low, gtemp_level_high, gtemp_level_low, glight_level_high, glight_level_low
    global high, low, sensor_type
    text = "{} graph".format(type)

    if type == 'Light':
        ser.flush()
        ser.write(bytes('L', 'UTF-8'))
        sensor_type = 'Light'
        high = glight_level_high
        low = glight_level_low
    if type == 'Moisture':
        ser.flush()
        ser.write(bytes('M', 'UTF-8'))
        sensor_type = 'Moisture'
        high = gwater_level_high
        low = gwater_level_low
    if type == 'Temperature':
        ser.flush()
        ser.write(bytes('T', 'UTF-8'))
        sensor_type = 'Temperature'
        high = gtemp_level_high
        low = gtemp_level_low
    if s == False:
        swi()
    global reading_variable
    reading_variable = True

    Thread1 = Thread(target=collect_data, daemon=True)
    Thread1.start()

    graph_label.delete("1.0", tk.END)
    graph_label.insert("1.0", text)




# create the label for the graph which switches depending on which button is pressed

graph_label = Text(window, bd=0, width=36, height=1, bg=colour_dark, fg="white", font="Arial")
graph_label.place(x=129.5, y=185)

# to create multiple buttons with different commands use a dictionary
for i in range(len(Categories)):
    def function(x=Categories[i]):
        xs.clear()
        ys.clear()
        global counter
        counter = 0
        return entry_update(x)


    button_dict[i] = tk.Button(window, text=Categories[i], bd=0, font="Arial", bg=colour_dark, fg="white", height=4,
                               width=10, command=function)
    button_dict[i].place(x=0, y=i * height / len(Categories))




sensors = ["Light", "Moisture", "Temperature"]

sensor_button_dict = {}

for i in range(len(sensors)):
    def function1(x=sensors[i]):
        q.queue.clear()
        xs.clear()
        ys.clear()
        global counter
        counter = 0
        return graph_update(x)


    sensor_button_dict[i] = tk.Button(window, text=sensors[i], bd=0, font="Arial", bg=colour_dark, fg="white", height=5,
                                      width=18, command=function1)
    sensor_button_dict[i].place(x=(i + 1) * (width - 115) / len(sensors) - 100, y=50)







# Create command for on off switch
def swi():
    global s
    if s: # On going to off
        with q.mutex:
            q.queue.clear()
            q.all_tasks_done.notify_all()
            q.unfinished_tasks = 0
        s = False
        print("sending X")
        ser.write(bytes('X', 'UTF-8'))
        global reading_variable
        reading_variable = False
        #sensor_data.clear()
        switch.configure(text = "OFF" , bg = "lightgrey", fg="black")
        graph_label.delete("1.0", tk.END)

    
    else: # off going to on 3
        s = True
        xs.clear()
        ys.clear()
        switch.configure(text = "ON", bg = "palegreen", fg="white")

# Create On off button
switch = tk.Button(window, text="OFF", bd=0, font = "Arial", bg="lightgrey", fg="black", height = 1, width = 10, command=swi)
switch.place(x=450, y=5)




def collect_data():
    global reading_variable
    print(reading_variable)
    while (reading_variable == True):
        print("hello")
        print(s)
        if (s == False):
            break
        print(ser.in_waiting)
        if (ser.in_waiting > 0):

            getData = ser.readline()
            dataString = int(getData.decode('utf-8'))
            q.put(dataString)


    #window.after(100, collect_data)




style.use('ggplot')
bar1 = None

xs = []
ys = []
global counter
counter = 0


def animate():
    global bar1
    global counter
    global high, low


    if (q.qsize() >0):
        item = q.get()
        ys.append(item)
        print("appending data")
        print(ys)
        counter = counter + 1
        xs.append(counter)
        q.task_done()



    fig = Figure(figsize=(4,3.8), dpi = 100)
    ax1 = fig.add_subplot(1,1,1)
    ax1.axhline(y=high, color='r', linestyle='--')
    ax1.axhline(y=low, color='r', linestyle='--')
    ax1.plot(xs, ys)
    if bar1:
        bar1.get_tk_widget().pack_forget()

    bar1 = FigureCanvasTkAgg(fig, window)
    bar1.draw()
    bar1.get_tk_widget().place(x=130, y=210)
    window.after(100, animate)

#Thread2 = Thread(target = animate)
#Thread2.start()

# Create an animated graph
q.join()
ser = serial.Serial("COM4", 9600)

#window.after(1000, collect_data)

window.after(100, animate)

# create a drop down list to select the port input
com_label = tk.Label(window, text="select COM port", bg=colour_dark, fg="white", font="Arial")
com_label.place(x = 120, y = 10)

n = tk.StringVar()

com_combobox = ttk.Combobox(window, width = 20, textvariable = n)

com_combobox['values'] = list(serial.tools.list_ports.comports())

com_combobox.place(x= 280, y = 13)

window.geometry(text)
window.mainloop()
