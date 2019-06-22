
def remove_duplicates(L1, L2):

	# Making a clone of list L1
	# L1_Copy points to a different objects with L1 contents
	L1_copy = L1[:]

	for e in L1_copy:

		if e in L2:
			L1.remove(e)
	return L1

result = remove_duplicates([1, 2, 3, 4], [1, 2, 5, 6])
print("Resultant list values: "+str(result))