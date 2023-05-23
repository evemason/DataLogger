# Importing Libraries
import serial
import time
import tkinter
arduino = serial.Serial(port='COM4', baudrate=9600, timeout=0.1)
arduino.write(bytes('f', 'utf-8'))

def set_button1_state():
        global b
        b += 1
        varLabel.set("LED ON ")
        arduino.write(bytes('H', 'UTF-8'))
        varLabel2.set(b)
        print(b)

tkTop = tkinter.Tk()
tkTop.geometry('300x200')
tkTop.title("IoT24hours")
label3 = tkinter.Label(text = 'Building Python GUI to interface an arduino,'
                      '\n and control an LED',font=("Courier", 12,'bold')).pack()
tkTop.counter = 0
b = tkTop.counter

varLabel = tkinter.IntVar()
tkLabel = tkinter.Label(textvariable=varLabel, )
tkLabel.pack()

varLabel2 = tkinter.IntVar()
tkLabel2 = tkinter.Label(textvariable=varLabel2, )
tkLabel2.pack()

button1 = tkinter.IntVar()
button1state = tkinter.Button(tkTop,
    text="ON",
    command=set_button1_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button1state.pack(side='top', ipadx=10, padx=10, pady=15)

tkinter.mainloop()