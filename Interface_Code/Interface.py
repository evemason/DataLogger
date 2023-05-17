from tkinter import *
import matplotlib.pyplot as plt


Categories = 6

window = Tk()

window.title("Plant Care System")
window.configure(bg='darkseagreen')

width = 800
height = 600
XPOS = 350
YPOS = 100

text = str(width) + "x" + str(height) + "+" + str(XPOS) + "+" + str(YPOS)



for i in range(Categories):
    btn = Button(window, text = "Cactus", bd = 0, font= "Arial", bg = "darkseagreen3", fg = "white", relief=GROOVE, height= 4, width = 10)
    btn.place(x = 0, y = i * height/Categories) 
    i = i + 1

sensors = ["Light", "Moisture", "Temperature"]

for i in range(len(sensors)):
    btn1 = btn = Button(window, text = sensors[i], bd = 0, font= "Arial", bg = "darkseagreen3", fg = "white", height= 5, width = 15)
    btn1.place(x = (i+1)*(width-100)/len(sensors) - 95, y = 10) 



window.geometry(text)
window.mainloop()