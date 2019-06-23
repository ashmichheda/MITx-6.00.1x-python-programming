import string

def getAvailableLetters(lettersGuessed):

	lower_alphabets = string.ascii_lowercase
	val = ""

	for i in lower_alphabets:
		if i not in lettersGuessed:
			val = val + i
	return val


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
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getGuessedWord(secretWord, lettersGuessed):

	val = ""

	for i in secretWord:
		if i not in lettersGuessed:
			val = val + "_ "
		else:
			val = val + i

	return val

print("Welcome to the game of hangman!")
print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
lines = "-----------"
print(lines)
guesses = 8
lettersGuessed = []

while isWordGuessed(secretWord,lettersGuessed)==False and guesses!=0:
	print("You have {} guesses left.".format(guesses))
	print("Available Letters: {}".format(getAvailableLetters(lettersGuessed)))
	usrInp = input("Please guess a letter: ").lower()
	if usrInp in lettersGuessed:
		print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed)))
	elif usrInp in secretWord:
		lettersGuessed.append(usrInp)
		print("Good guess: "+str(getGuessedWord(secretWord, lettersGuessed)))
	else:
		lettersGuessed.append(usrInp)
		guesses -= 1
		print("Oops! That letter is not in my word: {}".format(getGuessedWord(secretWord, lettersGuessed)))
	print(lines)

if guesses == 0:
	print("Sorry, you ran out of guesses. The word was {}".format(secretWord))
else:
	print("Congratulations, you won!")

