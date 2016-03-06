"""

Takes given team and presents stats from 2014 world cup.

Author: Joe Noel (noelj)

"""

def stats(team):
    
    #creates list of indexes of games team participated in
    i = 0
    index = []
    while i < len(results):
        if team.lower() == results[i][0].lower() or\
           team.lower() == results[i][2].lower():
            index.append(i)
        i += 1
        
    print "All games:"
    
    #prints team, scores, and victor
    i = 0
    for x in index:
        print results[x][0].rjust(24) + str(results[x][1]).rjust(4) + "-" +\
              str(results[x][3]).ljust(4) + results[x][2].ljust(24) +\
              "Winner:" + results[x][4]
    
    print "Scores:"
    print "Games".ljust(6) + "Win".ljust(6) + "Lose".ljust(6) +\
          "Draw".ljust(6) + "GF".ljust(6) + "GA".ljust(6)
    
    #computes and prints combined stats
    games = len(index)
    wins = 0
    for x in index:
        if team.lower() == results[x][4].lower():
            wins += 1
    draws = 0
    for x in index:
        if results[x][4].lower() == 'draw':
            draws += 1
    losses = games - wins - draws
    GF = 0
    for x in index:
        if results[x][0].lower() == team.lower():
            GF += results[x][1]
        elif results[x][2].lower() == team.lower():
            GF += results[x][3]
    GA = 0
    for x in index:
        if results[x][0].lower() != team.lower():
            GA += results[x][1]
        elif results[x][2].lower() != team.lower():
            GA += results[x][3]
    
    print str(games).ljust(6) + str(wins).ljust(6) + str(losses).ljust(6) +\
          str(draws).ljust(6) + str(GF).ljust(6) + str(GA).ljust(6)
    
    #determines and prints highest group, and the rank if top 4
    rank = ""
    if games == 0:
        highest = "not making it to the tournament"
    if games <= 3 and games > 0:
        highest = "group games"
    elif games == 4:
        highest = "round of 16"
    elif games == 5:
        highest = "quarter finals"
    elif games == 7 and results[index[-2]][4].lower() != team.lower():
        highest = "third place playoff"
        if (wins+draws) == 6:
            rank = "\nThis country placed in the third place"
        else:
            rank = "\nThis country placed in the fourth place"
    elif games == 7:
        highest = "finals"
        if (wins+draws) == 7:
            rank = "\nThis country placed in the first place"
        else:
            rank = "\nThis country placed in the second place"
    print "The highest achievment in 2014 World cup was %s%s" %(highest,rank)
    
###############
## Main Code ##
###############

import hw4_util
results = hw4_util.read_games('all_games.txt')

team = raw_input('Please enter a country ==> ')
print team

stats(team)