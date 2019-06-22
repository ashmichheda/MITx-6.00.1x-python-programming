
def how_many(animals):

	result = 0
	for val in animals.values():
		result += len(val)
	return result



animals = {'a':['aardvark'],'b':['baboon'],'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

answer = how_many(animals)
print("The no. of values are: "+str(answer))