import serial
import time
import tkinter as tk
#bytes_high = (400).to_bytes(2, byteorder = 'big')
#bytes_low = (100).to_bytes(2, byteorder = 'big')

window = tk.Tk()
datah2 = '40'
datah3 = '400'
datah4 = '4000'

datal2 = '20'
datal3 = '200'
datal4 = '2000'

def send2():
    ser.write(bytes('I', 'UTF-8'))
    ser.write(bytes(str(len(datah2)), 'UTF-8'))
    for i in range(len(datah2)):
        ser.write(bytes(datah2[i], 'UTF-8'))
    ser.write(bytes(str(len(datal2)), 'UTF-8'))
    for i in range(len(datal2)):
        ser.write(bytes(datal2[i], 'UTF-8'))


button = tk.Button(text="data2", command = send2)
button.pack()


def send3():
    ser.write(bytes('I', 'UTF-8'))
    ser.write(bytes(str(len(datah3)), 'UTF-8'))
    for i in range(len(datah3)):
        ser.write(bytes(datah3[i], 'UTF-8'))
    ser.write(bytes(str(len(datal3)), 'UTF-8'))
    for i in range(len(datal3)):
        ser.write(bytes(datal3[i], 'UTF-8'))


button = tk.Button(text="data3", command = send3)
button.pack()

def send4():
    ser.write(bytes('I', 'UTF-8'))
    ser.write(bytes(str(len(datah4)), 'UTF-8'))
    for i in range(len(datah4)):
        ser.write(bytes(datah4[i], 'UTF-8'))
    ser.write(bytes(str(len(datal4)), 'UTF-8'))
    for i in range(len(datal4)):
        ser.write(bytes(datal4[i], 'UTF-8'))
 


button = tk.Button(text="data4", command = send4)
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
