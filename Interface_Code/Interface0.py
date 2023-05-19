from tkinter import *
from matplotlib.figure import Figure
import numpy as np
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sb

colour_light = "palegreen3"
colour_dark = "palegreen4"

Categories = np.array(["Cactus", "Tropical", "Alpine", "Bulbs", "Climbers", "Ferns"])

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


for i in range(len(Categories)):
    btn = Button(window, text = Categories[i], bd = 0, font= "Arial", bg = colour_dark, fg = "white", height= 4, width = 10)
    btn.place(x = 0, y = i * height/len(Categories))
    i = i + 1

sensors = ["Light", "Moisture", "Temperature"]

for i in range(len(sensors)):
    btn1 = btn = Button(window, text = sensors[i], bd = 0, font= "Arial", bg = colour_dark, fg = "white", height= 5, width = 18)
    btn1.place(x = (i+1)*(width-115)/len(sensors) - 100, y = 50) 


window.geometry(text)
window.mainloop()