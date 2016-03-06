"""
A program to take a restaurant from a list and print some of it's information.

Author: Joe Noel (noelj)
"""

import lab04_util

def print_info(restaurant):
    print restaurant[0] + " (%s)" %(restaurant[-2])
    address = restaurant[3]
    address = address.split("+")
    print "\t" + address[0]
    print "\t" + address[1]
    average = sum(restaurant[-1])/float(len(restaurant[-1]))
    print "Average Score: %.2f" %(average)

##################
#### Main Code ###
##################

restaurant = lab04_util.read_yelp('yelp.txt')
print_info(restaurant[0])
