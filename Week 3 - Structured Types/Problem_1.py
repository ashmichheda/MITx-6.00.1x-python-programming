def isWordGuessed(secretWord, lettersGuessed):

	count = 0
	for i in secretWord:
		if i in lettersGuessed:
			count += 1

	print('Final count value: '+str(count))
	if count == len(secretWord):
		return True
	else:
		return False


secretWord = 'apple'
lettersGuessed = ['a', 'l', 'e', 'p', 'r', 's']
result = isWordGuessed(secretWord, lettersGuessed)
print("Is the word Guessed? " + str(result))
