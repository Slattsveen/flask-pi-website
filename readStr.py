import serial

name = 'ACM0'
msg = " "
#name = raw_input("Which port is the Arduino connected to?")
ser = serial.Serial('/dev/tty'+name, 9600)

cont = 1
while cont:
	msg = (ser.readline())
	if msg.split(' ').count('4'):
		cont = 0
	else:
		print(msg)
	


