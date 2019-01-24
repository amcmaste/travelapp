from flask import render_template, flash, redirect, request, jsonify
from app import app
from app.forms import InputForm
from app.reservations import reservation_bank
from app.functions import lookup

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])

def index():
	form = InputForm()
	
	for item in reservation_bank:
		print(item.confirmation)
		
	return render_template('form.html', form=form)

@app.route('/retreive', methods=['POST'])
def retreive():
	form = InputForm()
	data = request.form['confirmation']
	exists = False
	
	for item in reservation_bank:
		if str(data).lower() == str(item.confirmation).lower():
			exists = True
		else:
			pass
	
	if exists == True:
		print ("The reservation exists!")
	elif exists == False:
		print("The reservation does not exist.")
	else:
		print ("There was an error.")
		
	return render_template('form.html', form=form)