"""
Regular Expressions (sometimes shortened to regexp, regex, or re) 
are a tool for matching patterns in text. In Python, we have the re module. 
The applications for regular expressions are wide-spread, but they are fairly complex, 
so when contemplating using a regex for a certain task, think about alternatives, 
and come to regexes as a last resort.

http://www.learnpython.org/en/Regular_Expressions
"""

### EXAMPLES
import re

def do_the_examples():
	print "### EXAMPLES"
	pattern = re.compile(r"\[(on|off)\]")	# Slight optimization
	print re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]")
	# Returns a Match object!
	print re.search(pattern, "Nada...:-(")
	# Doesn't return anything.


"""
### EXERCISE

Make a regular expression that will match an email.
"""
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print "You failed to match %s" % (email)
        elif not your_pattern:
            print "Forgot to enter a pattern!"
        else:
            print "Pass"

def do_the_exercise():
	print "\n### EXERCISE"
	# Your pattern here!
	pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
	test_email(pattern)


do_the_examples()
do_the_exercise()

