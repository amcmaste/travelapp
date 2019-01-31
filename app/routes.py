#Imports
from flask import render_template, request, jsonify
from app import app
from app.forms import AddReservation, LookupReservation
from app.functions import write_db, read_db

#Routes
@app.route('/', methods=['GET'])
def home():
	return render_template('home.html')
	
@app.route('/input', methods=['GET', 'POST'])
def input():
	inputform = AddReservation()
	return render_template('inputform.html', form=inputform)
	
@app.route('/add', methods=['GET', 'POST'])
def add():
	result = write_db(request.form['confirmation'], request.form['type'],
					  request.form['company'], request.form['start_date'], 
					  request.form['end_date'], request.form['cost'])
	return result
	
@app.route('/output', methods=['GET', 'POST'])
def output():
	outputform = LookupReservation()
	return render_template('outputform.html', form=outputform)
	
@app.route('/lookup', methods=['GET', 'POST'])
def lookup():
	result = read_db(request.form['confirmation'])
	return result