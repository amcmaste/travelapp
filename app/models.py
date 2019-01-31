#Imports
from app import db

#Database models
class Reservation(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	confirmation = db.Column(db.String(10), unique=True, index=True)
	type =  db.Column(db.String(10))
	company = db.Column(db.String(10))
	start_date = db.Column(db.Date)
	end_date = db.Column(db.Date)
	cost = db.Column(db.Float)
	
	def __repr__(self):
		return '<Confirmation: {}>'.format(self.confirmation)