from flask import render_template, flash, redirect, request
from app import app
from app.forms import InputForm
from app.reservations import Reservations

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	code = ""
	form = InputForm()
	
	if request.method == 'POST' and form.validate_on_submit():
		code = request.form['confirmation']
		return render_template('index.html', form=form, code=code)
	else:
		return render_template('index.html', form=form, code=code)