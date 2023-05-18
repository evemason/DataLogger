from tkinter import *
from matplotlib.figure import Figure
import numpy as np
from LiveGraph import animate
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

colour_light = "palegreen3"
colour_dark = "palegreen4"

Categories = np.array(["Cactus", "Tropical", "Alpine", "Bulbs", "Climbers", "Ferns"])

window = Tk()
window.title("Plant Care System")
window.configure(bg=colour_light)


style.use('ggplot')
fig = Figure(figsize=(4,4), dpi=100)
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('Sample.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)

bar1 = FigureCanvasTkAgg(fig, window)
bar1.get_tk_widget().place(x=130, y=185)

width = 800
height = 620
XPOS = 350
YPOS = 100

text = str(width) + "x" + str(height) + "+" + str(XPOS) + "+" + str(YPOS)

'''
for i in range(len(Categories)):
    btn = Button(window, text = Categories[i], bd = 0, font= "Arial", bg = colour_dark, fg = "white", height= 4, width = 10)
    btn.place(x = 0, y = i * height/len(Categories))
    i = i + 1'''

sensors = ["Light", "Moisture", "Temperature"]
'''
for i in range(len(sensors)):
    btn1 = btn = Button(window, text = sensors[i], bd = 0, font= "Arial", bg = colour_dark, fg = "white", height= 5, width = 18)
    btn1.place(x = (i+1)*(width-115)/len(sensors) - 100, y = 50) '''


class Interface:
    def __init__(self, master):
        container = Frame(master)
        container.pack(side = "left", fill = "both")
        container.grid_columnconfigure(0, weight =1)
        container.grid_rowconfigure(0, weight =1)

        for i in range(len(Categories)):
            btn = Button(container, text = Categories[i], bd = 0, font= "Arial", bg = colour_dark, fg = "white", width = 10, height=4)
            btn.pack(side=TOP, expand=True)

        for i in range(len(sensors)):
            btn1 = btn = Button(window, text = sensors[i], bd = 0, font= "Arial", bg = colour_dark, fg = "white", height= 5, width = 18)
            btn1.place(x = (i+1)*(width-115)/len(sensors) - 100, y = 50) 



        

    #def clicker(self):
     #   print("Look you clicked a button!")




app = Interface(window)

window.geometry(text)
window.mainloop()