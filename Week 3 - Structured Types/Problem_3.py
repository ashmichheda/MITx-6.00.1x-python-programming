import string

def getAvailableLetters(lettersGuessed):

	lower_alphabets = string.ascii_lowercase
	val = ""

	for i in lower_alphabets:
		if i not in lettersGuessed:
			val = val + i
	return val

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
result = getAvailableLetters(lettersGuessed)
print("Available letters are: "+str(result))