
def biggest(animals):

	# returns: The key with the largest numbers of values associated with it
	largest_value = 0
	key_val = ""

	for key in animals.keys():

		if len(animals[key]) >= largest_value:
			key_val = key
			largest_value = len(animals[key])

	print("Largest key: "+str(key_val))


animals = {'a':['aardvark'],'b':['baboon'],'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
biggest(animals)