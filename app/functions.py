#Imports
from app import db
from app.models import Reservation

#Functions
def write_db(confnum):
	#Add new entry
	entry = Reservation(confirmation=confnum)
	db.session.add(entry)
	db.session.commit()
	
	#Verify that new entry has been added
	result = Reservation.query.filter_by(confirmation=confnum).first()
	return result.confirmation
	
def read_db(confnum):
	result = Reservation.query.filter_by(confirmation=confnum).first()
	return result.confirmation