from flask import render_template, flash, redirect, request, jsonify
from app import app
from app.forms import InputForm
from app.reservations import reservation_bank
from app.functions import lookup

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index():
	form = InputForm()
	
	for item in reservation_bank:
		print(item.confirmation)
		
	return render_template('form.html', form=form)

@app.route('/retrieve', methods=['GET', 'POST'])
def retrieve():
	data = request.form['number']
	
	for item in reservation_bank:
		if str(data).lower() == str(item.confirmation).lower():
			data = lookup(item.confirmation, reservation_bank)
			return jsonify({'type': data})
		else:
			pass
			
	return jsonify({'type': 'Reservation Not Found'})