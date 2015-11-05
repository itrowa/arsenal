number = 23
running = True

while running:
	guess = int(raw_input('Enter a integer : '))
	
	if guess == number:
		print 'Congratulations, you guessed it.'
		running = False
	elif guess < number:
		print 'No, it is a little higher than that'
	else:
		print 'No, it is a little lower than that.'
else:
	print 'The whole loop is over. Thank you.'
	
print 'Done.'