#Imports
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired

#Form definition
class AddReservation(FlaskForm):
	confirmation = StringField('Confirmation', validators=[DataRequired()])
	type = SelectField('Type', choices=[('airline', 'Airline'), ('hotel', 'Hotel'), 
		('car', 'Car')])
	company = StringField('Company')
	start_date = StringField('Start Date')
	end_date = StringField('End Date')
	cost = IntegerField('Cost')
	submit = SubmitField('Submit')

class LookupReservation(FlaskForm):
	confirmation = StringField('Confirmation', validators=[DataRequired()])
	submit = SubmitField('Submit')