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
gwater_level_high = 0
gwater_level_low = 0
gtemp_level_high = 0
gtemp_level_low = 0
glight_level_high = 0
glight_level_low = 0
high = 0
low = 0
sensor_data = []
new_data = 0 


colour_light = "palegreen3"
colour_dark = "palegreen4"

Categories = ["Tropical", "Cactus", "Alpine", "Bulbs", "Climbers", "Ferns"]

window = Tk()

window.title("Plant Care System")
window.configure(bg=colour_light)

# create queues for the sensor values
q = queue.Queue()


'''style.use('ggplot')
bar1 = None

# Create an animated graph

def animate(data):
    global bar1
    global high, low
    h = np.empty(len(data))
    h.fill(high)
    l = np.empty(len(data))
    l.fill(low)
    xs = []
    ys = []
    for points in data:
        if len(data) > new_data:
            xs.append(new_data)
            ys.append(data)
            new_data = new_data + 1
    fig = Figure(figsize=(4, 3.8), dpi=100)
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(xs, data)
    ax1.plot(xs,l)
    ax1.plot(xs,h)

    if bar1:
        bar1.get_tk_widget().pack_forget()

    bar1 = FigureCanvasTkAgg(fig, window)
    bar1.draw()
    bar1.get_tk_widget().place(x=130, y=210)
    window.after(100, animate(data))


window.after(1, animate(sensor_data))

# ani = animation.FuncAnimation(fig, animate, interval=1000)

# bar1 = FigureCanvasTkAgg(fig, window)
# bar1.get_tk_widget().place(x=130, y=185)'''


width = 800
height = 600
XPOS = 350
YPOS = 100

text = str(width) + "x" + str(height) + "+" + str(XPOS) + "+" + str(YPOS)

data = pd.read_csv(r'Database\Plant_data.csv')

#print(data)
Categories = ["Tropical", "Cactus", "Alpine", "Bulbs", "Climbers", "Ferns"]
# I don't think we need this any more
water_high = data['water_high'].tolist()
water_low = data['water_low'].tolist()
temp_high = data['temp_high'].tolist()
temp_low = data['temp_low'].tolist()
light_high = data['light_high'].tolist()
light_low = data['light_low'].tolist()

# I also think we don't need this 
def extract_data(plant_name):
    index = Categories.index(plant_name)
    water_level_high = water_high[index]
    water_level_low = water_low[index]
    temp_level_low = temp_low[index]
    temp_level_high = temp_high[index]
    light_level_low = light_low[index]
    light_level_high = light_high[index]

    return water_level_high, water_level_low, temp_level_high, temp_level_low, light_level_high, light_level_low


def entry_update(name):
    global gwater_level_high, gwater_level_low, gtemp_level_high, gtemp_level_low, glight_level_high, glight_level_low
    gwater_level_high, gwater_level_low, gtemp_level_high, gtemp_level_low, glight_level_high, glight_level_low = Database.extract_all(name)
    text = extract_data(name)
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
    global high, low
    text = "{} graph".format(type)
    if type == 'Light':
        ser.write(bytes('L', 'UTF-8'))
        high = glight_level_high
        low = glight_level_low
    if type == 'Moisture':
        ser.write(bytes('M', 'UTF-8'))
        high = gwater_level_high
        low = gwater_level_low
    if type == 'Temperature':
        ser.write(bytes('T', 'UTF-8'))
        high = gtemp_level_high
        low = gtemp_level_low
    if s == False:
        swi()
    global reading_variable
    reading_variable = True
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
        sensor_data.clear()
        return graph_update(x)


    sensor_button_dict[i] = tk.Button(window, text=sensors[i], bd=0, font="Arial", bg=colour_dark, fg="white", height=5,
                                      width=18, command=function1)
    sensor_button_dict[i].place(x=(i + 1) * (width - 115) / len(sensors) - 100, y=50)







# Create command for on off switch
def swi():
    global s
    if s: # On going to off
        s = False
        print("sending X")
        ser.write(bytes('X', 'UTF-8'))
        global reading_variable
        reading_variable = False
        sensor_data.clear()
        switch.configure(text = "OFF" , bg = "lightgrey", fg="black")
        graph_label.delete("1.0", tk.END)
    
    else: # off going to on 
        s = True
        switch.configure(text = "ON", bg = "palegreen", fg="white")

# Create On off button
switch = tk.Button(window, text="OFF", bd=0, font = "Arial", bg="lightgrey", fg="black", height = 1, width = 10, command=swi)
switch.place(x=450, y=5)




def collect_data():
    global reading_variable
    if (reading_variable == True):

        if (ser.in_waiting > 0):
            getData = ser.readline()
            dataString = int(getData.decode('utf-8'))
            sensor_data.append(dataString)
            print(sensor_data)
            q.put(dataString)

    window.after(100, collect_data)

Thread1 = Thread(target= collect_data)
Thread1.start()

style.use('ggplot')
bar1 = None

xs = []
ys = []
global counter
counter = 0

h = np.empty(len(data))
h.fill(high)
l = np.empty(len(data))
l.fill(low)

h = []
l = []

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
        h.append(high)
        l.append(low)


    fig = Figure(figsize=(4,3.8), dpi = 100)
    ax1 = fig.add_subplot(1,1,1)
    ax1.plot(xs, ys)
    ax1.plot(xs, l)
    ax1.plot(xs, h)
    if bar1:
        bar1.get_tk_widget().pack_forget()

    bar1 = FigureCanvasTkAgg(fig, window)
    bar1.draw()
    bar1.get_tk_widget().place(x=130, y=210)
    window.after(100, animate)

Thread2 = Thread(target = animate)
Thread2.start()

# Create an animated graph
'''
def animate(data):
    global bar1
    global high, low
    h = np.empty(len(data))
    h.fill(high)
    l = np.empty(len(data))
    l.fill(low)
    xs = []
    ys = []
    for points in data:
        if len(data) > new_data:
            xs.append(new_data)
            ys.append(data)
            new_data = new_data + 1
    fig = Figure(figsize=(4, 3.8), dpi=100)
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(xs, data)
    ax1.plot(xs,l)
    ax1.plot(xs,h)

    if bar1:
        bar1.get_tk_widget().pack_forget()

    bar1 = FigureCanvasTkAgg(fig, window)
    bar1.draw()
    bar1.get_tk_widget().place(x=130, y=210)
    window.after(100, animate(data))


window.after(1, animate(sensor_data))
'''

q.join()
ser = serial.Serial("COM4", 9600)

#window.after(1000, collect_data)

# create a drop down list to select the port input
com_label = tk.Label(window, text="select COM port", bg=colour_dark, fg="white", font="Arial")
com_label.place(x = 120, y = 10)

n = tk.StringVar()

com_combobox = ttk.Combobox(window, width = 20, textvariable = n)

com_combobox['values'] = list(serial.tools.list_ports.comports())

com_combobox.place(x= 280, y = 13)

window.geometry(text)
window.mainloop()
