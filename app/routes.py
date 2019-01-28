#Reworked

#Imports
from flask import render_template
from app import app

#Routes
@app.route('/', methods=['GET'])
def home():
	return render_template('home.html')
	
@app.route('/input', methods=['GET'])
def input():
	return render_template('input.html')
	
@app.route('/output', methods=['GET'])
def output():
	return render_template('output.html')