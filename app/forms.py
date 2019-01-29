#Reworked

#Imports
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired

#Form definition
class AddReservation(FlaskForm):
	confirmation = StringField('Confirmation', validators=[DataRequired()])
	type = SelectField('Type', choices=[('airline', 'Airline'), ('hotel', 'Hotel'), 
		('car', 'Car')], validators=[DataRequired()])
	company = StringField('Company', validators=[DataRequired()])
	startdate = DateField('Start Date', id="start_date", validators=[DataRequired()])
	enddate = DateField('End Date', id="end_date", validators=[DataRequired()])
	cost = IntegerField('Cost', validators=[DataRequired()])
	submit = SubmitField('Submit', validators=[DataRequired()])

class LookupReservation(FlaskForm):
	confirmation = StringField('Confirmation', validators=[DataRequired()])
	submit = SubmitField('Submit', validators=[DataRequired()])