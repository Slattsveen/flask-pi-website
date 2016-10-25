from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

#GPIO stuff
GPIO.setmode(GPIO.BOARD)
ledPin = 7
GPIO.setup(ledPin, GPIO.OUT)

def blink(num):
	for i in range(0, num):
		GPIO.output(ledPin, True)
		time.sleep(1)
		GPIO.output(ledPin, False)
		time.sleep(1)
	print("done blinking")
	GPIO.cleanup()


#server stuff:

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/press')
def press():
	blink(4)
	return render_template('jQuery_pressB.html')

if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0')


