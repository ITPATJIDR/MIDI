import serial
from manager_MIDI.serialInput import SerialInput

ser = serial.Serial('/dev/ttyACM0', 9600)  
input = SerialInput()

while True:
    input.setNewData(ser.readline().strip())



