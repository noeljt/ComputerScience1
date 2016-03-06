"""
A program to compute standings based upon possible game results.

Author: Joe Noel (noelj)
"""

def winner(stats1,stats2,score):
    #calculates who won and changes stats based upon result
    
    stats1l = []
    for x in stats1:
        stats1l.append(int(x))
        
    stats2l = []
    for x in stats2:
        stats2l.append(int(x))
                       
    if score[0] > score[1]:
        stats1l[0] += 1
        stats1l[-2] += score[0]
        stats1l[-1] += score[1]
        stats2l[1] += 1
        stats2l[-2] += score[1]
        stats2l[-1] += score[0]
    elif score[1] > score[0]:
        stats2l[0] += 1
        stats2l[-2] += score[1]
        stats2l[-1] += score[0]
        stats1l[1] += 1
        stats1l[-2] += score[0]
        stats1l[-1] += score[1]
    elif score[0] == score[1]:
        stats1l[2] += 1
        stats1l[-2] += score[0]
        stats1l[-1] += score[1]
        stats2l[2] += 1
        stats2l[-2] += score[1]
        stats2l[-1] += score[0] 
    
    #calculates which team is ranked higher
    Pts1 = 3 * stats1l[0] + stats1l[2]
    Pts2 = 3 * stats2l[0] + stats2l[2]
    Gdiff1 = stats1l[-2] - stats1l[-1]
    Gdiff2 = stats2l[-2] - stats2l[-1]
    GF1 = stats1l[-2]
    GF2 = stats2l[-2]
    if Pts1 > Pts2:
        return 1
    elif Pts2 > Pts1:
        return 2
    elif Pts1 == Pts2:
        if Gdiff1 > Gdiff2:
            return 1
        elif Gdiff2 > Gdiff1:
            return 2
        elif Gdiff1 == Gdiff2:
            if GF1 > GF2:
                return 1
            elif GF2 > GF1:
                return 2
            elif GF1 == GF2:
                return 0

def print_info(s1,s2):
    stats1 = s1.split(',')
    stats2 = s2.split(',')
    print "Columns are team 1 goals, rows are team 2 goals"
    print "Goals|" + "0".center(5) + "1".center(5) + "2".center(5) +\
          "3".center(5) + "4".center(5)
    print "-----|" + "-" * 25
    for x in range(5):
        print "  %d  |" %(x) + str(winner(stats1,stats2,(0,x))).center(5) +\
              str(winner(stats1,stats2,(1,x))).center(5) +\
              str(winner(stats1,stats2,(2,x))).center(5) +\
              str(winner(stats1,stats2,(3,x))).center(5) +\
              str(winner(stats1,stats2,(4,x))).center(5)

###############
## Main Code ##
###############

s1 = raw_input('Enter team 1 stats ==> ')
print s1
s2 = raw_input('Enter team 2 stats ==> ')
print s2

print_info(s1,s2)