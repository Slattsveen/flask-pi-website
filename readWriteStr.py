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
	

print("Send anything to turn on LED, send 0 to turn it off")

while True:
	msg = raw_input("send 1 to turn LED on, send 0 to turn off")
	ser.write(msg)
	print("I sent message: " + msg)
