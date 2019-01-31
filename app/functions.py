#Imports
from app import db
from app.models import Reservation
from datetime import datetime
from flask import jsonify

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
	return jsonify({'confirmation': result.confirmation, 'type': result.type, 'company': result.company, 
			'start_date': result.start_date, 'end_date': result.end_date, 'cost': result.cost})
	
def read_db(confnum):
	result = Reservation.query.filter_by(confirmation=confnum).first()
	return jsonify({'confirmation': result.confirmation, 'type': result.type, 'company': result.company, 
			'start_date': result.start_date, 'end_date': result.end_date, 'cost': result.cost})