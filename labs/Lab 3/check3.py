"""
Prints a given word with a "frame".

Author: Joe Noel (noelj)
"""

word = raw_input("Enter a four letter word: ")
print word

def framed(word):
    print "*" * (len(word) + 6)
    print "** " + word + " **"
    print "*" * (len(word) + 6)

framed (word)