from tkinter import *
import tkinter as tk
from matplotlib.figure import Figure
import numpy as np
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sb
import pandas as pd

colour_light = "palegreen3"
colour_dark = "palegreen4"

Categories = ["Cactus", "Tropical", "Alpine", "Bulbs", "Climbers", "Ferns"]

window = Tk()

window.title("Plant Care System")
window.configure(bg=colour_light)


style.use('ggplot')
#fig = Figure(figsize=(4,4), dpi=100)
#ax1 = fig.add_subplot(1,1,1)

bar1=None

def animate():
    global bar1
    graph_data = open('Sample.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    fig = Figure(figsize=(4,4), dpi=100)
    ax1 = fig.add_subplot(1,1,1)
    ax1.plot(xs,ys)

    if bar1: 
        bar1.get_tk_widget().pack_forget()

    bar1 = FigureCanvasTkAgg(fig,window)
    bar1.draw()
    bar1.get_tk_widget().place(x=130, y=185)
    window.after(100,animate)

window.after(1,animate)

#ani = animation.FuncAnimation(fig, animate, interval=1000)

#bar1 = FigureCanvasTkAgg(fig, window)
#bar1.get_tk_widget().place(x=130, y=185)


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
    entry.insert("1.0",text)


entry = Text(window, bd = 0, width = 25, height = 22)
entry.place(x = 550, y = 220)

recommendations = Label(window, text = "Plant care recommendations", bg = colour_dark, fg = "white", width = 28)
recommendations.place(x = 550, y = 200)

button_dict= {}

#to create multiple buttons with different commands use a dictionary
for i in range(len(Categories)):
    def function(x = Categories[i]):
        return entry_update(x)

    button_dict[i] = tk.Button(window, text = Categories[i], bd = 0, font = "Arial", bg = colour_dark, fg = "white", height = 4, width = 10 ,command = function)
    button_dict[i].place(x=0, y = i *height/len(Categories))

''' 
for i in range(len(Categories)):
    btn = Button(window, text = Categories[i], bd = 0, font= "Arial", bg = colour_dark, fg = "white", height= 4, width = 10)
    btn.place(x = 0, y = i * height/len(Categories))
    i = i + 1
'''
sensors = ["Light", "Moisture", "Temperature"]

for i in range(len(sensors)):
    btn1 = btn = Button(window, text = sensors[i], bd = 0, font= "Arial", bg = colour_dark, fg = "white", height= 5, width = 18)
    btn1.place(x = (i+1)*(width-115)/len(sensors) - 100, y = 50) 


window.geometry(text)
window.mainloop()