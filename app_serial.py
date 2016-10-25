import serial, datetime
from flask import Flask, render_template, request
app = Flask(__name__)


#Serial definitions:
name = 'ACM0'
ser = serial.Serial('/dev/tty'+name, 9600)

@app.route('/')
def index():
	now = datetime.datetime.now()
	timeStr = now.strftime("%H:%M")

	webData = {'time' : timeStr}

	return render_template('main.html', **webData)


@app.route('/sendMsg/<msg>')
def sendMsg(msg):
	ser.write(msg)
	now = datetime.datetime.now()
	timeStr = now.strftime("%H:%M")

	webData = {'time' : timeStr, 'msg' : msg}

	return render_template('main.html', **webData)

if __name__ == "__main__":
	app.run(host = "0.0.0.0", debug = True)
