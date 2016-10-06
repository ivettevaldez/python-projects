"""
As you can see, the first thing you learned was printing a simple sentence. 
This sentence was stored by Python as a string. 
However, instead of immediately printing strings out, we will explore 
the various things you can do to them. You can also use single quotes to assing a string. 
However, you will face problems if the value to be assigned itself contains single quotes.

http://www.learnpython.org/en/Basic_String_Operations
"""

### EXAMPLES

print "### EXAMPLES"
print "Single quotes are ' '"

# This prints out 12, because "Hello world!" is 12 characters long, including punctuation and spaces.
astring = "Hello world!"
print len(astring)

# This prints out 4, because the location of the first occurrence of the letter "o" is 4 characters away from the first character. 
print astring.index("o")

# This counts the number of l's in the string. Therefore, it should print 3.
print astring.count("l")

# This prints a slice of the string, starting at index 3, and ending at index 6.
print astring[3:7]

# This prints the characters of string from 3 to 7 skipping two characters. This is extended slice syntax. The general form is [start:stop:step].
print astring[3:7:2]

# You can easily reverse a string like this:
print astring[::-1]

# These make a new string with all letters converted to uppercase and lowercase, respectively.
print astring.upper()
print astring.lower()

# This is used to determine whether the string starts with something or ends with something, respectively.
print astring.startswith("Hello")
print astring.endswith("asdfasdfasdf")

# This splits the string into a bunch of strings grouped together in a list. 
afewwords = astring.split(" ")
print afewwords


"""
### EXERCISE

Try to fix the code to print out the correct information by changing the string.
"""
print "\n### EXERCISE"

s = "Strings are awesome!"
# Length should be 20
print "Length of s = %d" % len(s)

# First occurrence of "a" should be at index 8
print "The first occurrence of the letter a = %d" % s.index("a")

# Number of a's should be 2
print "a occurs %d times" % s.count("a")

# Slicing the string into bits
print "The first five characters are '%s'" % s[:5] # Start to 5
print "The next five characters are '%s'" % s[5:10] # 5 to 10
print "The thirteenth character is '%s'" % s[12] # Just number 12
print "The characters with odd index are '%s'" %s[1::2] #(0-based indexing)
print "The last five characters are '%s'" % s[-5:] # 5th-from-last to end

# Convert everything to uppercase
print "String in uppercase: %s" % s.upper()

# Convert everything to lowercase
print "String in lowercase: %s" % s.lower()

# Check how a string starts
if s.startswith("Str"):
    print "String starts with 'Str'. Good!"

# Check how a string ends
if s.endswith("ome!"):
    print "String ends with 'ome!'. Good!"

# Split the string into three separate strings,
# each containing only a word
print "Split the words of the string: %s" % s.split(" ")


