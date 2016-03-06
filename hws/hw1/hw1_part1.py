"""
Computes the percentage increase each day in posts with hashtags related to the ice bucket challenge.

Author: Joe Noel (noelj)
"""

def percent_change(x,y):
    return int((float(y-x) / x) * 100)

print "#icebucketchallenge vs #alsicebucketchallenge, percentage change"
print percent_change(200,500), "vs", percent_change(100,300)
print percent_change(500,2000), "vs", percent_change(300,1500)
print percent_change(2000,12000), "vs", percent_change(1500,13000)
print percent_change(12000,24000), "vs", percent_change(13000, 25000)
print percent_change(24000,65000), "vs", percent_change(25000,105000)
print percent_change(65000,70000), "vs", percent_change(105000,85000)