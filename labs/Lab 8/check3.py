"""
Program to find similar clubs within the Union.

Author: Joe Noel (noelj)
"""

#returns set of words from string
def get_words_s(string1):
    desc = string1
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

#returns set of words from file
def get_words_f(file1):
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

#finds 5 most similar clubs based upon similar words
def similarity(file1):
    club1_words = get_words_f(file1)
    all_clubs = open('allclubs.txt').read().split('\n')
    del all_clubs[-1]
    index = []
    for club in all_clubs:
        club_split = club.split('|')
        club2_words = get_words_s(club_split[1])
        common = len(club1_words & club2_words)
        index.append((common, club_split[0]))
    index.sort(reverse=True)
    print "Top 5 similar clubs:"
    for x in range(6):
        if x == 0:
            continue
        print "%d)" %(x), index[x][1]
        
###############
## Main Code ##
###############

file1 = raw_input('Club Name ==> ') + '.txt'
similarity(file1)