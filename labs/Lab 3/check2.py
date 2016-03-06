"""
Prints a given 4 letter word with a "frame".

Author: Joe Noel (noelj)
"""

word = raw_input("Enter a four letter word: ")
print word

def framed(word):
    print '*' * 10
    print '** %s **' %(word)
    print '*' * 10

framed (word)