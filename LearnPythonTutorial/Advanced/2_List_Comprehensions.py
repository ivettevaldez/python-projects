"""
List Comprehensions is a very powerful tool, which creates a new list 
based on another list, in a single, readable line.

http://www.learnpython.org/en/List_Comprehensions
"""

### EXAMPLES

def do_the_examples():
	print "### EXAMPLES"
	"""
	Let's say we need to create a list of integers which specify the length 
	of each word in a certain sentence, but only if the word is not the word "the".
	"""
	sentence = "the quick brown fox jumps over the lazy dog"
	words = sentence.split()
	word_lengths = []
	for word in words:
	    if word != "the":
	        word_lengths.append(len(word))

	print word_lengths

	# Using a list comprehension, we could simplify this process to this notation:
	sentence = "the quick brown fox jumps over the lazy dog"
	words = sentence.split()
	word_lengths = [len(word) for word in words if word != "the"]

	print word_lengths


"""
### EXERCISE

Using a list comprehension, create a new list called "newlist" out of the list "numbers", 
which contains only the positive numbers from the list, as integers.
"""
def do_the_exercise():
	print "\n### EXERCISE"

	numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
	newlist = [int(x) for x in numbers if x >= 0]

	print newlist


do_the_examples()
do_the_exercise()

