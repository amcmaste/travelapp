#Reworked

#Imports
from flask import render_template
from app import app
from app.forms import AddReservation, LookupReservation

#Routes
@app.route('/', methods=['GET'])
def home():
	return render_template('home.html')
	
@app.route('/input', methods=['GET'])
def input():
	inputform = AddReservation()
	return render_template('inputform.html', form=inputform)
	
@app.route('/output', methods=['GET'])
def output():
	outputform = LookupReservation()
	return render_template('outputform.html', form=outputform)