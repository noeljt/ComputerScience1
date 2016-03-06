"""
Program to compare words used in two clubs' descriptions.

Author: Joe Noel (noelj)
"""

def get_words(file1):
    f = open(file1)
    f2 = f.read().split('|')
    desc = f2[1]
    desc = desc.replace(',','').replace('.','').replace('\(','')\
        .replace('\)','').replace('\"','').lower()
    desc = desc.split()
    rl = []
    for x in desc:
        if len(x) < 4 or x.isalpha() == False:
            rl.append(x)
    for x in rl:
        desc.remove(x)
    desc2 = set(desc)
    return desc2

###############
## Main Code ##
###############

club1 = raw_input('First Club Name ==> ') + '.txt'
club2 = raw_input('Second Club Name ==> ') + '.txt'

words1 = get_words(club1)
words2 = get_words(club2)
common = words1 & words2
unique1 = words1 - words2
unique2 = words2 - words1

print "Words in common:\n", common
print "Words unique to %s club:\n" %(club1.replace('.txt','')) + str(unique1)
print "Words unique to %s club:\n" %(club2.replace('.txt','')) + str(unique2)
