#Imports
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField

#Form definition
class AddReservation(FlaskForm):
	confirmation = StringField('Confirmation', id="confirmation", validators=[DataRequired(), Length(1, 6)])
	type = SelectField('Type', id="type", choices=[('airline', 'Airline'), ('hotel', 'Hotel'), 
					  ('car', 'Car')], validators=[DataRequired()])
	company = StringField('Company', id="company", validators=[DataRequired(), Length(1,10)])
	start_date = DateField('Start Date', id="start_date", format='%Y-%m-%d', validators=[DataRequired()])
	end_date = DateField('End Date', id="end_date", format='%Y-%m-%d', validators=[DataRequired()])
	cost = DecimalField('Cost', id="cost", places=2, validators=[DataRequired()])
	submit = SubmitField('Submit', id="submit")

class LookupReservation(FlaskForm):
	confirmation = StringField('Confirmation', validators=[DataRequired()])
	submit = SubmitField('Submit')