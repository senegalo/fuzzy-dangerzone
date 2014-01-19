import serial
import sys 

ser = serial.Serial('/dev/ttyACM0',9600)

ser.close()
ser.open()

msg = sys.argv[1]+"#"
print msg
ser.write(msg.encode('ascii'))
