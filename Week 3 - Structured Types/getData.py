
def get_data(inputTuple):
    nums = ()
    words = ()
    for t in inputTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    print("Inside method")
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)

    return min_nums, max_nums, unique_words


(small, large, unWords) = get_data(((1, "yours"),
                                   (2, "mine"),
                                   (3, "ours"),
                                   (4, "ours")))
print("Smallest number: " + str(small))
print("Largest number: " + str(large))
print("No. of unique words: " + str(unWords))
