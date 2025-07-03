#numbers_set = {1, 2, 3, 4, 4}  Duplicates are not allowed
#numbers_set = {1, 2, 3, 4, [5, 6]}  Cannot use mutable types
#numbers_set = {1, 2, 3, 4, (5, 6)}  Tuples are immutable, OK to use
#print(numbers_set)

words_set = {"Alpha", "Bravo", "Charlie"}
""" abcd = ""
for word in words_set:
    abcd += word
print(abcd) """

""" if "Alpha" in words_set:
    print("Alpha is in the set")
else:
    print("Alpha is not in the set") """

words_set.add("Delta")
print(words_set)
words_set.discard("Bravo")
print(words_set)