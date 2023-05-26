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
from threading import Thread

# Global variables
s = False
reading_variable = False

colour_light = "palegreen3"
colour_dark = "palegreen4"

Categories = ["Cactus", "Tropical", "Alpine", "Bulbs", "Climbers", "Ferns"]

window = Tk()

window.title("Plant Care System")
window.configure(bg=colour_light)

style.use('ggplot')
# fig = Figure(figsize=(4,4), dpi=100)
# ax1 = fig.add_subplot(1,1,1)

bar1 = None

# Create an animated graph that reads a csv file

def animate():
    global bar1
    graph_data = open('Sample.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    fig = Figure(figsize=(4, 3.8), dpi=100)
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(xs, ys)

    if bar1:
        bar1.get_tk_widget().pack_forget()

    bar1 = FigureCanvasTkAgg(fig, window)
    bar1.draw()
    bar1.get_tk_widget().place(x=130, y=210)
    window.after(100, animate)


window.after(1, animate)

# ani = animation.FuncAnimation(fig, animate, interval=1000)

# bar1 = FigureCanvasTkAgg(fig, window)
# bar1.get_tk_widget().place(x=130, y=185)


width = 800
height = 600
XPOS = 350
YPOS = 100

text = str(width) + "x" + str(height) + "+" + str(XPOS) + "+" + str(YPOS)

data = pd.read_csv(r'Database\Plant_data.csv')

print(data)
Categories = ["Cactus", "Tropical", "Alpine", "Bulbs", "Climbers", "Ferns"]

water_high = data['water_high'].tolist()
water_low = data['water_low'].tolist()
temp_high = data['temp_high'].tolist()
temp_low = data['temp_low'].tolist()
light_high = data['light_high'].tolist()
light_low = data['light_low'].tolist()


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
    text = extract_data(name)
    entry.delete("1.0", tk.END)
    entry.insert("1.0", text)


entry = Text(window, bd=0, width=25, height=22)
entry.place(x=550, y=220)

recommendations = Label(window, text="Plant care recommendations", bg=colour_dark, fg="white", width=28)
recommendations.place(x=550, y=200)

button_dict = {}


# create a function which updates the label of the graph
def graph_update(type):
    global s
    text = "{} graph".format(type)
    if type == 'Light':
        ser.write(bytes('L', 'UTF-8'))
    if type == 'Moisture':
        ser.write(bytes('M', 'UTF-8'))
    if type == 'Temperature':
        ser.write(bytes('T', 'UTF-8'))
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
        ser.write(bytes('X', 'UTF-8'))
        global reading_variable
        reading_variable = False
        sensor_data.clear()
        switch.configure(text = "OFF" , bg = "lightgrey", fg="black")
    
    else: # off going to on 
        s = True
        switch.configure(text = "ON", bg = "palegreen", fg="white")

# Create On off button
switch = tk.Button(window, text="OFF", bd=0, font = "Arial", bg="lightgrey", fg="black", height = 1, width = 10, command=swi)
switch.place(x=450, y=5)




sensor_data = []
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



# create a drop down list to select the port input
com_label = tk.Label(window, text="select COM port", bg=colour_dark, fg="white", font="Arial")
com_label.place(x = 120, y = 10)

n = tk.StringVar()

com_combobox = ttk.Combobox(window, width = 20, textvariable = n)

com_combobox['values'] = list(serial.tools.list_ports.comports())

com_combobox.place(x= 280, y = 13)

window.geometry(text)
window.mainloop()