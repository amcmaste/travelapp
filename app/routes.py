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
	
@app.route('/add', methods=['POST'])
def add():
	result = write_db(request.form['confirmation'])
	return jsonify({'entry': result})
	
@app.route('/output', methods=['GET', 'POST'])
def output():
	outputform = LookupReservation()
	return render_template('outputform.html', form=outputform)
	
@app.route('/lookup', methods=['POST'])
def lookup():
	result = read_db(request.form['confirmation'])
	return jsonify({'entry': result})