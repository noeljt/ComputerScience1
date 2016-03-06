"""
A program to compute a record, total points, and goal advantage for a soccer team.

Author: Joe Noel (noelj)
"""

def record_and_points(team, wins, losses, draws, goals_for, goals_against):
    points = wins * 3+draws
    goal_adv = goals_for - goals_against
    print team
    print "Win:", wins, "Lose:", losses, "Draw:", draws
    print "Total number of points:", points, "Goal advantage:", goal_adv

record_and_points("Germany", 2, 1, 0, 7, 2)
record_and_points("USA", 1, 1, 1, 4, 4)
record_and_points("Argentina", 3, 0, 0, 6, 3)
record_and_points("England", 0, 1, 2, 2, 4)