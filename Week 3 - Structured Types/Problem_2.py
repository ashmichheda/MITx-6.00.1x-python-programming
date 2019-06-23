
def getGuessedWord(secretWord, lettersGuessed):

	val = ""

	for i in secretWord:
		if i not in lettersGuessed:
			val = val + "_ "
		else:
			val = val + i

	return val


secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
result = getGuessedWord(secretWord, lettersGuessed)
print("Is the word Guessed? " + str(result))