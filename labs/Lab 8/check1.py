"""
Function to take club info and create list of words used.

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
    print "File", file1, len(desc2), 'words'
    print desc2

###############
## Main Code ##
###############

file1 = raw_input('File Name ==> ')
get_words(file1)