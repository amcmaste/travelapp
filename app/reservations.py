class Reservations(object):
	
	def __init__(self, confirmation, name):
		self.confirmation = confirmation
		self.name = name
		
	def create_dummies():
		A = Reservations('123456', 'Airline Reservation')
		B = Reservations('654321', 'Hotel Reservation')
		return [A, B]