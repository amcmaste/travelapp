def retrieve(confnum, reservations):
	for reservation in reservations:
		if reservation.confirmation == confnum:
			return reservation.type
		else:
			continue
	return None