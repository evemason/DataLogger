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
import tkinter as tk
import numpy as np
from threading import Thread
import queue
from Databaseclass import Database
import tkinter.font as fnt


# Global variables
s = False #this a variable to determine the state of the system on or off.
reading_variable = False # this is to determine whether data should be collected from the arduino

# the following global variables are read from the database to determine the ideal levels
gwater_level_high = Database.water_level_high('Tropical')
gwater_level_low = Database.water_level_low('Tropical')
gtemp_level_high = Database.temp_level_high('Tropical')
gtemp_level_low = Database.temp_level_low('Tropical')
glight_level_high = Database.light_level_high('Tropical')
glight_level_low = Database.light_level_low('Tropical')

# values to plot on the graph for the high and low levels
high = 0
low = 0

# variable to say which sensor button has been pressed
sensor_type = 'off'

# variables used to update the plant care recommendations
check_light = 3
check_moist = 3
check_temp = 3

# variables for the colour scheme
colour_light = "palegreen3"
colour_dark = "palegreen4"

# catagories of different plant types to create different buttons
Categories = ["Tropical", "Cactus", "Alpine", "Bulbs", "Climbers", "Ferns"]


# create the window using tkinter
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


'''function which implements the communication protocol when a plate type button is pressed based on which sensor button
 has been pressed it also updates the high and low levels based on the type of plant desired to plot on the graph'''
def entry_update(name):
    global gwater_level_high, gwater_level_low, gtemp_level_high, gtemp_level_low, glight_level_high, glight_level_low

    # extracts the information about the ideal levels from the database based on the plant type
    gwater_level_high, gwater_level_low, gtemp_level_high, gtemp_level_low, glight_level_high, glight_level_low = Database.extract_all(name)
    global sensor_type, high, low

    # converts the integers from the data base to be strings so they can be iterable and send on serial
    # communication as desired
    high_string = str(glight_level_high)
    low_string = str(glight_level_low)

    if sensor_type == 'Light':
        high = glight_level_high
        low = glight_level_low
        # sends the information flag so the arduino knows the following data is from the database
        ser.write(bytes('I', 'UTF-8'))

        # sends the length of the string for the high light level
        ser.write(bytes(str(len(high_string)), 'UTF-8'))

        # iterates over each of the characters and sends them along the serial communication
        for i in range(len(high_string)):
            ser.write(bytes(high_string[i], 'UTF-8'))

        # sends the length of the string for the low light level
        ser.write(bytes(str(len(low_string)), 'UTF-8'))

        # iterates over each of the characters in low_string and sends them along serial communication
        for i in range(len(low_string)):
            ser.write(bytes(low_string[i], 'UTF-8'))

        #once the information has been sent a 'L' is send to
        ser.write(bytes('L', 'UTF-8'))

    if sensor_type == 'Temperature':
        high = gtemp_level_high
        low = gtemp_level_low
        ser.write(bytes('T', 'UTF-8'))
    if sensor_type == 'Moisture':
        high = gwater_level_high
        low = gwater_level_low
        ser.write(bytes('M', 'UTF-8'))





'''function which is called when a sensor type button is pressed. It uses which sensor button is pressed to implement 
the communication protocol. If the switch button is off then it goes into the swi function'''
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

    #if the system is off go into swi
    if s == False:
        swi()

    if type == 'Light':
        #send the information to the arduino from the database which will be used to control the arduino
        ser.write(bytes('I', 'UTF-8'))
        ser.write(bytes(str(len(high_string)), 'UTF-8'))
        for i in range(len(high_string)):
            ser.write(bytes(high_string[i], 'UTF-8'))
        ser.write(bytes(str(len(low_string)), 'UTF-8'))
        for i in range(len(low_string)):
            ser.write(bytes(low_string[i], 'UTF-8'))
        ser.write(bytes('L', 'UTF-8'))
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

    # update the text above the graph to illustrate which graph it is i.e. light, temp or moisture
    graph_label.delete("1.0", tk.END)
    graph_label.insert("1.0", text)


# create the label for the graph which switches depending on which button is pressed
graph_label = Text(window, bd=0, width=36, height=1, bg=colour_dark, fg="white", font="Arial")
graph_label.place(x=129.5, y=185)

# initialise a dictionary of plant type buttons
button_dict = {}

# to create multiple buttons with different commands use a dictionary the buttons each have a slightly different
# function depending on their name this can be done by using a for loop
for i in range(len(Categories)):
    def function(x=Categories[i]):

        # empty the queue when a different button is pressed
        q.queue.clear()
        q.unfinished_tasks = 0

        # clear the graph
        xs.clear()
        ys.clear()

        #sendings the information light levels in entry_update
        global counter
        counter = 0
        return entry_update(x)

    # creates the buttons on the interface
    button_dict[i] = tk.Button(window, text=Categories[i], bd=0, font="Arial", bg=colour_dark, fg="white", height=4,
                               width=10, command=function)
    button_dict[i].place(x=0, y=i * height / len(Categories))



# an array of the different type of sensors
sensors = ["Light", "Moisture", "Temperature"]

# initialises a dictionary to have the sensor buttons in
sensor_button_dict = {}


# to create multiple buttons with different commands use a dictionary the buttons each have a slightly different
# function depending on their name this can be done by using a for loop
for i in range(len(sensors)):
    def function1(x=sensors[i]):
        # clears the queue when a different button is pressed
        q.queue.clear()
        q.unfinished_tasks = 0

        # clears the graph
        xs.clear()
        ys.clear()
        global counter
        counter = 0
        return graph_update(x)

    #creates the buttons on the interface
    sensor_button_dict[i] = tk.Button(window, text=sensors[i], bd=0, font="Arial", bg=colour_dark, fg="white", height=5,
                                      width=18, command=function1)
    sensor_button_dict[i].place(x=(i + 1) * (width - 115) / len(sensors) - 100, y=50)







# Create command for on off switch
def swi():
    global s

    if s == False: # off going to on
        print("on")
        s = True
        # start the thread to collect data from the serial connection
        Thread1 = Thread(target=collect_data, daemon=True)
        Thread1.start()
        print("sending X")
        ser.write(bytes('X', 'UTF-8'))

        #clears the graph
        xs.clear()
        ys.clear()
        switch.configure(text = "ON", bg = "palegreen", fg="white")

    else: # On going to off

        q.queue.clear()
        q.unfinished_tasks = 0
        s = False
        print("sending X")
        ser.write(bytes('X', 'UTF-8'))
        global reading_variable
        #stops reading the data
        reading_variable = False
        switch.configure(text = "OFF" , bg = "lightgrey", fg="black")

        #not sure we want to delete the graph label need to test
        graph_label.delete("1.0", tk.END)


'''function to read the incoming data from the serial this happens in a thread so it is important to use a queue 
to put the data in '''
def collect_data():
    global reading_variable
    print("thread started")

    # collect data if a sensor button has been pressed
    while (reading_variable == True):
        #print("collecting data")
        #stops collecting data if has been turned off
        if (s == False):
            break

        # checks there is something waiting in the serial port before reading the data
        if (ser.in_waiting > 0):

            getData = ser.readline()
            data = getData.decode('utf-8')
            print(data)
            # converts the incoming string to an integer
            dataString = int(data)

            # puts the data into the queue
            q.put(dataString)





style.use('ggplot')
bar1 = None


# initialise arrays to store the data from the queue in to plot on the graph
xs = []
ys = []
global counter
counter = 0

'''function to create the live graph and update the plant care recommendations'''
def animate():
    global bar1
    global counter
    global high, low
    global sensor_type
    global check_temp, check_light, check_moist

    # if there is something in the queue collect the data
    if (q.qsize() >0):
        item = q.get()

        print("from queue is: ", item)
        #append this data to the array
        ys.append(item)
        xs.append(counter - 2)


        # these if statements are for the plant care recommendations
        if (sensor_type == 'Light'):
            # want light recommendation
            # set the other check variables to 3 so that if a different button is pressed the text will be updated
            check_moist = 3
            check_temp = 3
            if (item > high):
                # only replace the text if it has changed
                if (check_light != 0):
                    text2 = 'Put in a shadier spot'
                    check_light = 0
                    entry.delete("1.0", tk.END)
                    entry.insert("1.0", text2)
            if (item < low):
                if (check_light != 1):
                    text = 'Put in a sunnier spot'
                    check_light = 1
                    entry.delete("1.0", tk.END)
                    entry.insert("1.0", text)
            if(item>=low and item<=high):
                if (check_light != 2):
                    text1 = 'Perfect light conditions for this plant'
                    check_light = 2
                    entry.delete("1.0", tk.END)
                    entry.insert("1.0", text1)

        elif (sensor_type == 'Moisture'):
            # want light recommendation
            check_light = 3
            check_temp = 3
            if (item > high):
                if (check_moist != 0):
                    text = 'Dry out the soil'
                    check_moist = 0
                    entry.delete("1.0", tk.END)
                    entry.insert("1.0", text)

            if (item < low):
                if (check_moist != 1):
                    text = 'Water the plant'
                    check_moist = 1
                    entry.delete("1.0", tk.END)
                    entry.insert("1.0", text)
            if(item>=low and item<=high):
                if (check_moist != 2):
                    # the spaces are so the words stay as a whole
                    text1 = 'Perfect moisture             conditions for this plant'
                    check_moist = 2
                    entry.delete("1.0", tk.END)
                    entry.insert("1.0", text1)


        elif (sensor_type == 'Temperature'):
            # want light recommendation
            check_light = 3
            check_moist = 3
            if (item > high):
                if (check_temp != 0):
                    text = 'Put in a cooler place'
                    check_temp = 0
                    entry.delete("1.0", tk.END)
                    entry.insert("1.0", text)

            if (item < low):
                if (check_temp != 1):
                    text = 'Put in a warmer place'
                    check_temp = 1
                    entry.delete("1.0", tk.END)
                    entry.insert("1.0", text)
            if(item>=low and item<=high):
                if (check_temp != 2):
                    text1 = 'Perfect temperature        conditions for this plant'
                    check_temp = 2
                    entry.delete("1.0", tk.END)
                    entry.insert("1.0", text1)

        # there is a delay in updating the queue correctly and therefore we add a delay so it only plots the data after
        # 2 have entered
        if (counter<2):
            ys.clear()
            xs.clear()
        # increment the counter to show data has been collected from the queue
        counter = counter + 1

        q.task_done()


    # creating the graph
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

    # this animates the graph
    window.after(50, animate)






# this animates the graph every 50ms
window.after(50, animate)

# create a drop down list to select the port input
com_label = tk.Label(window, text="select COM port", bg=colour_dark, fg="white", font="Arial")
com_label.place(x = 120, y = 10)

# this creates a label to title the text box where the plant care recommendations gets inserted
recommendations = Label(window, text="Plant care recommendations", bg=colour_dark, fg="white", width=26, height = 1,font = fnt.Font(size = 13))
recommendations.place(x=550, y=185)


# this is a text box where the plant care recommendation
entry = Text(window, bd=0, width=21, height=16, font = 'Arial', fg = colour_dark)
entry.place(x=550, y=210)

# Create On off button
switch = tk.Button(window, text="OFF", bd=0, font = "Arial", bg="lightgrey", fg="black", height = 1, width = 10, command=swi)
switch.place(x=450, y=5)


'''function to check which com ports are available and then update the com port drop down so the selection is from 
the available ones '''
def com_select():
    global clicked_com
    ports = serial.tools.list_ports.comports()
    coms = [com[0] for com in ports]

    clicked_com = StringVar()
    clicked_com.set(coms[0])

    # uses an option menu to have the drop down of possible com ports
    drop_coms = OptionMenu(window, clicked_com, *coms)
    drop_coms.config(width = 20,bd=0,bg="lightgrey")
    drop_coms.place(x = 280, y =11)


com_select()

com_port = clicked_com.get()
print(com_port)

# uses the serial connection based on the one selected in the com port drop down
ser = serial.Serial(com_port, 9600)

window.geometry(text)
window.mainloop()