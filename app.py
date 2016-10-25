from flask import Flask, render_template



#server stuff:

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/press')
def press():
	
	return render_template('jQuery_pressB.html')

if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0')


