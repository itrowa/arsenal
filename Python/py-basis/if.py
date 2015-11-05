number = 23
guess = int(raw_input('Enter a integer : '))

if guess == number:
	print 'Congratulations, you guessed it.'
	print 'But you wont win any prizes!!!'
elif guess < number:
	print 'No, it is a little higher than that.'
else:
	print 'No, it is a little lower than that.'
	
print 'Done'

	