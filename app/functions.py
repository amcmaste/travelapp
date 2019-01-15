def retrieve(confnum, reservations):
	for reservation in reservations:
		if reservation.confirmation == confnum:
			return reservation.name
		else:
			continue
	return None