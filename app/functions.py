#Imports
from app import db
from app.models import Reservation

#Functions
def write_db(number):
	entry = Reservation(confirmation=number)
	db.session.add(entry)
	db.session.commit()
	return number
	
def read_db(confirmation):
	result = str(Reservation.query.get(2))
	return result