import tkinter as tk
from tkinter import *

window = Tk()
window.title("Plant Care")
window.geometry("800x500")

class Interface:
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.myButton = Button(master, text = "Click Me!", command = self.clicker)
        self.myButton.pack(pady=20)
    
    def clicker(self):
        print("Look you clicked a button!")

w = Interface(window)


window.mainloop()