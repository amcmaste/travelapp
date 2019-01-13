from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class InputForm(FlaskForm):
	code = StringField('Confirmation Code', validators=[DataRequired(), Length(6,6)])
	submit = SubmitField('Submit')