from random import randint

class Reservations(object):
	
	def __init__(self, confirmation, type):
		self.confirmation = confirmation
		self.type = type
		
	def create_dummies(number=5):
	
		# create reservation
		reservations = []
		count = 0
		
		while count < number:
		
			# assign confirmation
			init_confirmation = []
			i = 0
			
			while i < 6:
				current = str(randint(0, 15))
				if current == '10':
					current = 'A'
				elif current == '11':
					current = 'B'
				elif current == '12':
					current = 'C'
				elif current == '13':
					current = 'D'
				elif current == '14':
					current = 'E'
				elif current == '15':
					current = 'F'
				else:
					pass
				
				init_confirmation.append(current)
				i += 1
				
			init_confirmation = ''.join(init_confirmation)
			
			# assign reservation type
			init_type = ''
			pointer = randint(0, 2)
			
			if pointer == 0:
				init_type = 'Airline Reservation'
			elif pointer == 1:
				init_type = 'Hotel Reservation'
			elif pointer == 2:
				init_type = 'Car Reservation'
			else:
				init_type = 'Error'
			
			reservation = Reservations(init_confirmation, init_type)
			
			reservations.append(reservation)
			
			count += 1

		return reservations
		
reservation_bank = Reservations.create_dummies()