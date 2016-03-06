"""
Program to compare any two FIFA teams.

Author: Joe Noel (noelj)
"""

import hw3_util
teams = hw3_util.read_fifa()
#[group id, country, games, win, draw, lose, goals scored, goals against]

def select_teams():
    t1 = int(raw_input("First team index (0-31) ==> "))
    print t1
    t2 = int(raw_input("Second team index (0-31) ==> "))
    print t2
    return (t1,t2)

def compare_teams( (t1,t2) ):
    team1 = teams[t1]
    team2 = teams[t2]
    Pts1 = 3 * team1[3] + team1[4]
    Pts2 = 3 * team2[3] + team2[4]
    Gdiff1 = team1[-2] - team1[-1]
    Gdiff2 = team2[-2] - team2[-1]
    GF1 = team1[-2]
    GF2 = team2[-2]
    if Pts1 > Pts2:
        print team1[1] + " is better than " + team2[1]
    elif Pts2 > Pts1:
        print team2[1] + " is better than " + team1[1]
    elif Pts1 == Pts2:
        if Gdiff1 > Gdiff2:
            print team1[1] + " is better than " + team2[1]
        elif Gdiff2 > Gdiff1:
            print team2[1] + " is better than " + team1[1]
        elif Gdiff1 == Gdiff2:
            if GF1 > GF2:
                print team1[1] + " is better than " + team2[1]
            elif GF2 > GF1:
                print team2[1] + " is better than " + team1[1]
            elif GF1 == GF2:
                print team2[1] + " same as " + team1[1]
    
def teams_info( (t1,t2) ):
    team1 = teams[t1]
    team2 = teams[t2]
    Gdiff1 = team1[-2] - team1[-1]
    Gdiff2 = team2[-2] - team2[-1]
    Pts1 = 3 * team1[3] + team1[4]
    Pts2 = 3 * team2[3] + team2[4]
    print "\nGroup " + "Team" + (" "*16) + "Win   Draw  Lose  GF    GA    Gdiff Pts   "
    print str(team1[0]).ljust(6) + team1[1].ljust(20) + str(team1[3]).ljust(6) + str(team1[4]).ljust(6) + str(team1[5]).ljust(6) + str(team1[-2]).ljust(6) + str(team1[-1]).ljust(6) + str(Gdiff1).ljust(6) + str(Pts1).ljust(6)
    print str(team2[0]).ljust(6) + team2[1].ljust(20) + str(team2[3]).ljust(6) + str(team2[4]).ljust(6) + str(team2[5]).ljust(6) + str(team2[-2]).ljust(6) + str(team2[-1]).ljust(6) + str(Gdiff2).ljust(6) + str(Pts2).ljust(6) 
    compare_teams( (t1,t2) )

teams_info(select_teams())