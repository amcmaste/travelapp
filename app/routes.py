#Reworked

#Imports
from flask import render_template, request, jsonify
from app import app
from app.forms import AddReservation, LookupReservation

#Routes
@app.route('/', methods=['GET'])
def home():
	return render_template('home.html')
	
@app.route('/input', methods=['GET', 'POST'])
def input():
	inputform = AddReservation()
	return render_template('inputform.html', form=inputform)
	
@app.route('/output', methods=['GET', 'POST'])
def output():
	outputform = LookupReservation()
	return render_template('outputform.html', form=outputform)
	
@app.route('/lookup', methods=['POST'])
def lookup():
	data = request.form['confirmation']
	return jsonify({'confirmation': data})