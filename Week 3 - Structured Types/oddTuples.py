def getOddTuples(inputTuple: object) -> object:
	tuple = ()

	inp: object
	for inp in inputTuple:
		# print(inp)
		if len(inp) % 2 != 0:
			tuple = tuple + (inp,)
	return tuple


resultTuple = getOddTuples(('I', 'am', 'a', 'test', 'tuple'))
print("The odd Tuple is: "+str(resultTuple))