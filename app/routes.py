from flask import render_template, flash, redirect, request
from app import app
from app.forms import InputForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		form = InputForm()
		return render_template('index.html', form=form)
	elif request.method =='POST':
		form = InputForm()
		if form.validate_on_submit():
			data = request.form['code']
			print(data)
			return render_template('index.html', form=form)
		else:
			return render_template('index.html', form=form)
	else:
		pass