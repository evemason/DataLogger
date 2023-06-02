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
check_light = 3
check_moist = 3
check_temp = 3
#Thread1 = Thread()

colour_light = "palegreen3"
colour_dark = "palegreen4"

Categories = ["Tropical", "Cactus", "Alpine", "Bulbs", "Climbers", "Ferns"]

window = Tk()

window.title("Plant Care System")
window.configure(bg=colour_light)

# create queues for the sensor values
q = queue.Queue()


#create a queue for the type of sensor



width = 800
height = 600
XPOS = 350
YPOS = 100

text = str(width) + "x" + str(height) + "+" + str(XPOS) + "+" + str(YPOS)

Categories = ["Tropical", "Cactus", "Alpine", "Bulbs", "Climbers", "Ferns"]


def entry_update(name):
    global gwater_level_high, gwater_level_low, gtemp_level_high, gtemp_level_low, glight_level_high, glight_level_low
    gwater_level_high, gwater_level_low, gtemp_level_high, gtemp_level_low, glight_level_high, glight_level_low = Database.extract_all(name)
    global sensor_type, high, low
    if sensor_type == 'Light':
        high = glight_level_high
        low = glight_level_low
        levels = str(high) + "a" + str(low)
        levels_string = str(levels)
        bytes_high = high.to_bytes(2, byteorder = 'big') #not used at the moment but could be useful to send the data
        bytes_low = low.to_bytes(2, byteorder = 'big')
        ser.write(bytes(str(high), 'utf-8'))
        ser.write(bytes('a', 'utf-8'))
        ser.write(bytes(str(low), 'utf-8'))
        #ser.write(bytes_high)
        #ser.write(bytes_low)

    if sensor_type == 'Temperature':
        high = gtemp_level_high
        low = gtemp_level_low
    if sensor_type == 'Moisture':
        high = gwater_level_high
        low = gwater_level_low




recommendations = Label(window, text="Plant care recommendations", bg=colour_dark, fg="white", width=28)
recommendations.place(x=550, y=200)

button_dict = {}


# create a function which is called when a sensor button is clicked
def graph_update(type):
    global s
    global gwater_level_high, gwater_level_low, gtemp_level_high, gtemp_level_low, glight_level_high, glight_level_low
    global high, low, sensor_type

    text = "{} graph".format(type)
    print("sensor button pressed")

    global reading_variable
    reading_variable = True

    high_string = str(glight_level_high)
    low_string = str(glight_level_low)

    if s == False:
        swi()
    if type == 'Light':
        ser.write(bytes('I', 'UTF-8'))
        ser.write(bytes(str(len(high_string)), 'UTF-8'))
        for i in range(len(high_string)):
            ser.write(bytes(high_string[i]), 'UTF-8')
        ser.write(bytes(str(len(low_string)), 'UTF-8'))
        for i in range(len(low_string)):
            ser.write(bytes(low_string[i], 'UTF-8'))
        print("sending L")
        ser.write(bytes('L', 'UTF-8'))
        sensor_type = 'Light'
        high = glight_level_high
        low = glight_level_low


    if type == 'Moisture':

        print("sending M")
        ser.write(bytes('M', 'UTF-8'))
        sensor_type = 'Moisture'
        high = gwater_level_high
        low = gwater_level_low

    if type == 'Temperature':

        print("sending T")
        ser.write(bytes('T', 'UTF-8'))
        sensor_type = 'Temperature'
        high = gtemp_level_high
        low = gtemp_level_low



    #Thread1 = Thread(target=collect_data, daemon=True)
    #Thread1.start()

    graph_label.delete("1.0", tk.END)
    graph_label.insert("1.0", text)





# create the label for the graph which switches depending on which button is pressed

graph_label = Text(window, bd=0, width=36, height=1, bg=colour_dark, fg="white", font="Arial")
graph_label.place(x=129.5, y=185)

# to create multiple buttons with different commands use a dictionary
for i in range(len(Categories)):
    def function(x=Categories[i]):
        q.queue.clear()
        q.unfinished_tasks = 0
        xs.clear()
        ys.clear()
        ser.write(bytes('I', 'utf-8'))
        #sendings the information light levels in entry_update
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
        #q.all_tasks_done.notify_all()
        q.unfinished_tasks = 0
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
    #global Thread1
    if s == False: # off going to on 3
        print("on")
        s = True
        Thread1 = Thread(target=collect_data, daemon=True)
        Thread1.start()
        #s = True
        xs.clear()
        ys.clear()
        switch.configure(text = "ON", bg = "palegreen", fg="white")

    else: # On going to off

        q.queue.clear()

        #q.all_tasks_done.notify_all()

        q.unfinished_tasks = 0
        s = False
        print("sending X")
        ser.write(bytes('X', 'UTF-8'))
        global reading_variable
        reading_variable = False
        #sensor_data.clear()
        switch.configure(text = "OFF" , bg = "lightgrey", fg="black")
        graph_label.delete("1.0", tk.END)
        #print(Thread1.is_alive())
        #if Thread1.is_alive():
        #    print("kill")
        #    Thread1.join()




# Create On off button
switch = tk.Button(window, text="OFF", bd=0, font = "Arial", bg="lightgrey", fg="black", height = 1, width = 10, command=swi)
switch.place(x=450, y=5)




def collect_data():
    global reading_variable
    print("thread started")
    while (reading_variable == True):
        #print("collecting data")
        if (s == False):
            break
        if (ser.in_waiting > 0):

            getData = ser.readline()
            data = getData.decode('utf-8')
            print(data)
            dataString = int(data)
            q.put(dataString)








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
    global sensor_type
    global check_temp, check_light, check_moist


    if (q.qsize() >0):
        item = q.get()

        print("from queue is: ", item)
        ys.append(item)
        xs.append(counter - 2)



        if (sensor_type == 'Light'):
            # want light recommendation
            check_moist = 3
            check_temp = 3
            if (item > high):
                if (check_light != 0):
                    text = 'put in a shadier spot'
                    check = 0
                    entry.delete("1.0", tk.END)
                    entry.insert("1.0", text)

            if (item < low):
                if (check_light != 1):
                    text = 'put in a sunnier spot'
                    check = 1
                    entry.delete("1.0", tk.END)
                    entry.insert("1.0", text)
            else:
                if (check_light != 2):
                    text1 = 'perfect light conditions for this plant'
                    check = 2
                    entry.delete("1.0", tk.END)
                    entry.insert("1.0", text1)

        elif (sensor_type == 'Moisture'):
            # want light recommendation
            check_light = 3
            check_temp = 3
            if (item > high):
                if (check_moist != 0):
                    text = 'dry out the soil'
                    check = 0
                    entry.delete("1.0", tk.END)
                    entry.insert("1.0", text)

            if (item < low):
                if (check_moist != 1):
                    text = 'water the plant'
                    check = 1
                    entry.delete("1.0", tk.END)
                    entry.insert("1.0", text)
            else:
                if (check_moist != 2):
                    text1 = 'perfect moisture conditions for this plant'
                    check = 2
                    entry.delete("1.0", tk.END)
                    entry.insert("1.0", text1)


        elif (sensor_type == 'Temperature'):
            # want light recommendation
            check_light = 3
            check_moist = 3
            if (item > high):
                if (check_temp != 0):
                    text = 'put in a cooler place'
                    check = 0
                    entry.delete("1.0", tk.END)
                    entry.insert("1.0", text)

            if (item < low):
                if (check_temp != 1):
                    text = 'put in a warmer place'
                    check = 1
                    entry.delete("1.0", tk.END)
                    entry.insert("1.0", text)
            else:
                if (check_temp != 2):
                    text1 = 'perfect temperature conditions    for this plant'
                    check = 2
                    entry.delete("1.0", tk.END)
                    entry.insert("1.0", text1)


        if (counter<2):
            ys.clear()
            xs.clear()
        counter = counter + 1


        q.task_done()


    #print(ys)

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
    window.after(50, animate)



# Create an animated graph
#q.join()


#window.after(1000, collect_data)

window.after(50, animate)

# create a drop down list to select the port input
com_label = tk.Label(window, text="select COM port", bg=colour_dark, fg="white", font="Arial")
com_label.place(x = 120, y = 10)

entry = Text(window, bd=0, width=25, height=22, font = 'Arial', fg = colour_dark)
entry.place(x=550, y=220)

def com_select():
    global clicked_com
    ports = serial.tools.list_ports.comports()
    coms = [com[0] for com in ports]
    #coms.insert(0, "COM4")


    clicked_com = StringVar()
    clicked_com.set(coms[0])
    drop_coms = OptionMenu(window, clicked_com, *coms)
    drop_coms.config(width = 20)
    drop_coms.place(x = 280, y =13)


com_select()

com_port = clicked_com.get()
print(com_port)

ser = serial.Serial(com_port, 9600)

window.geometry(text)
window.mainloop()