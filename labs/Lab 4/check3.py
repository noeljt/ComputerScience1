"""
A program to evaluate a restaurant based on reviews and provide restaurant info.

Author: Joe Noel (noelj)
"""
import webbrowser
import lab04_util

def print_info(restaurant):
    print restaurant[0] + " (%s)" %(restaurant[-2])
    address = restaurant[3]
    address = address.split("+")
    print "\t" + address[0]
    print "\t" + address[1]
    if len(restaurant[-1]) <= 3:
        average = sum(restaurant[-1])/float(len(restaurant[-1]))
    elif len(restaurant[-1]) > 3:
        average = (sum(restaurant[-1]) - max(restaurant[-1]) - min(restaurant[-1]))/float(len(restaurant[-1]) - 2)
    if average >= 0 and average < 2:
        print "This restaurant is rated bad, based on %d reviews." %(len(restaurant[-1]))
    elif average >= 2 and average < 3:
        print "This restaurant is rated average, based on %d reviews." %(len(restaurant[-1]))
    elif average >= 3 and average < 4:
        print "This restaurant is rated above average, based on %d reviews." %(len(restaurant[-1]))
    elif average >= 4 and average <= 5:
        print "This restaurant is rated very good, based on %d reviews." %(len(restaurant[-1]))
    print "\nWhat would you like to do next?\n1. Visit the homepage\n2. Show on Google Maps\n3. Show Directions to this restaurant"
    choice = int(raw_input("Your choice (1-3)? ==> "))
    if choice == 1:
        webbrowser.open(restaurant[-3])
    elif choice == 2:
        webbrowser.open('http://www.google.com/maps/place/' + restaurant[3]) 
    elif choice == 3:
        webbrowser.open('http://www.google.com/maps/dir/%s/110 8th Street Troy NY 12180' %(restaurant[3]))

def select_restaurant():
    selection = (int(raw_input("Enter a restaurant ID from 1 through 155 ==> ")) - 1)
    if selection < 0:
        print "Error\nNumber entered not within ID range.\n"
    elif selection > 154:
        print "Error\nNumber entered not within ID range.\n"
    else:
        return selection
    
##################
#### Main Code ###
##################

restaurant = lab04_util.read_yelp('yelp.txt')

print_info(restaurant[select_restaurant()])