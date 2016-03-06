"""
A program to decipher a given sentence.

Author: Joe Noel (noelj)
"""

sentence = raw_input("Please enter a sentence ==> ")
print sentence

def decipher(sentence):
    global sentence2
    sentence2 = " " + sentence
    sentence2 = sentence2.replace("rxr"," a")
    sentence2 = sentence2.replace("twt","o")
    sentence2 = sentence2.replace("yyy","u")
    sentence2 = sentence2.replace("xx","th")
    sentence2 = sentence2.replace("he","an")
    sentence2 = sentence2.replace("az az","e")
    sentence2 = sentence2.replace("bb","he")
    print "Deciphered as ==> %s" %(sentence2)

def count(sentence):
    decipher(sentence)
    s_sentence = sentence2.replace(" s","s")
    num_s = len(sentence2) - len(s_sentence)
    a_sentence = sentence2.replace(" a","a")
    num_a = len(sentence2) - len(a_sentence)
    c_sentence = sentence2.replace(" c","c")
    num_c = len(sentence2) - len(c_sentence)
    print "Number of words that start with s: " + str(num_s)
    print "Number of words that start with a: " + str(num_a)
    print "Number of words that start with c: " + str(num_c)

count(sentence)
