#Imports
from app import db
from app.models import Reservation
from datetime import datetime

#Functions
def write_db(con, typ, com, sta, end, cos):
	#Convert to Python datetime
	sta = datetime.strptime(sta, '%Y-%m-%d')
	end = datetime.strptime(end, '%Y-%m-%d')
	
	#Add new entry
	entry = Reservation(confirmation=con, type=typ, company=com, start_date=sta, 
					    end_date=end, cost=cos)
	db.session.add(entry)
	db.session.commit()
	
	#Verify that new entry has been added
	result = Reservation.query.filter_by(confirmation=con).first()
	return 'Entry ' + result.confirmation + ' added to database'
	
def read_db(confnum):
	result = Reservation.query.filter_by(confirmation=confnum).first()
	return 'Entry ' + result.confirmation + ' retreived from database'