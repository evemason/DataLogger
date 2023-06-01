import serial
import time
import tkinter as tk
#bytes_high = (400).to_bytes(2, byteorder = 'big')
#bytes_low = (100).to_bytes(2, byteorder = 'big')

window = tk.Tk()
data = '400'

def send():
    ser.write(bytes('I', 'UTF-8'))
    for i in range(len(data)):
        ser.write(bytes(data[i], 'UTF-8'))


button = tk.Button(text="press me", command = send)
button.pack()

ser = serial.Serial("COM4", 9600)
window.mainloop()



#ser.write(bytes_high, 2)
#ser.write(bytes('T', 'UTF-8'))

#data = [0, 0]
#counter = 0
'''
while True:
    #ser.write(bytes_high)
    ser.write(bytes('T', 'UTF-8'))
    if (ser.in_waiting>0):

        getData = ser.read()
        data = getData.decode('utf-8')
        print("from serial : ", data)
        #data[0] = data[1]
        #data[1] = getData
        #print("data array: ", data)
        '''
'''
        if counter >2:
            datastring = str(data[0])[:-1] + str(data[1])[2:]
            print("data string : ", datastring)
            number = int.from_bytes(datastring, byteorder = 'big')
            print(number)
            '''
