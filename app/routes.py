from flask import render_template, flash, redirect, request
from app import app
from app.forms import InputForm
from app.reservations import Reservations
from app.functions import retrieve

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	code = ""
	form = InputForm()
	res = Reservations.create_dummies()
	
	if request.method == 'POST' and form.validate_on_submit():
		reservation = retrieve(request.form['confirmation'], res)
		return render_template('reservation.html', reservation=reservation)
	else:
		return render_template('form.html', form=form, code=code)