import serial.tools.list_ports

ser = serial.Serial( port="/dev/pts/5", baudrate=115200)

def readSerial():
    while True:
        bytesToRead = ser.inWaiting()
        if (bytesToRead > 0):
            mess = ser.read(bytesToRead).decode("UTF-8")
            print(mess)


readSerial()