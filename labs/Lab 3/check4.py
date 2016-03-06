"""
Prints a greeting with a "frame" given a first and last name.

Author: Joe Noel (noelj)
"""

f_name = raw_input("Please enter your first name: ")
print f_name
l_name = raw_input("Please enter your last name: ")
print l_name

def greeting(f_name, l_name):
    l_name = "%s!" %(l_name)
    if len(f_name) <= 6 and len(l_name) <= 6:
        print "*" * (12)
        print "** Hello, **"
        print "**" + (" " * ((12 - 4 - len(f_name))/2)) + f_name + (" " * (len(f_name)%2)) + (" " * ((12 - 4 - len(f_name))/2)) + "**"
        print "**" + (" " * ((12 - 4 - len(l_name))/2)) + l_name + (" " * (len(l_name)%2)) + (" " * ((12 - 4 - len(l_name))/2)) + "**"
        print "*" * (12)
    elif len(f_name) > 6 and len(f_name) > len(l_name):
        top = "*" * (len(f_name) + 6)
        print top
        print "**" + (" " * ((len(top) - 10)/2)) + "Hello," + (" " * ((len(top) - 10)/2)) + (" " * (len(f_name)%2)) + "**"
        print "**" + (" " * ((len(top) - 4 - len(f_name))/2)) + f_name + (" " * ((len(top) - 4 - len(f_name))/2)) + "**"
        if (len(f_name)%2) == (len(l_name)%2):
            print "**" + (" " * ((len(top) - 4 - len(l_name))/2)) + l_name + (" " * ((len(top) - 4 - len(l_name))/2)) + "**"
        elif (len(l_name)%2) ==1 and (len(f_name)%2) != 1:
            print "**" + (" " * ((len(top) - 4 - len(l_name))/2)) + l_name + (" " * (len(l_name)%2)) + (" " * ((len(top) - 4 - len(l_name))/2)) + "**"
        else:
            print "**" + (" " * ((len(top) - 4 - len(l_name))/2)) + l_name + (" " * (len(top)%2)) + (" " * ((len(top) - 4 - len(l_name))/2)) + "**"
        print top
    elif len(l_name) > 6 and len(l_name) > len(f_name):
        top = "*" * (len(l_name) + 6)
        print top
        print "**" + (" " * ((len(top) - 10)/2)) + "Hello," + (" " * ((len(top) - 10)/2)) + (" " * (len(top)%2)) + "**"
        if (len(l_name)%2) == (len(f_name)%2):
            print "**" + (" " * ((len(top) - 4 - len(f_name))/2)) + f_name + (" " * ((len(top) - 4 - len(f_name))/2)) + "**"
        elif (len(f_name)%2) ==1 and (len(l_name)%2) != 1:
            print "**" + (" " * ((len(top) - 4 - len(f_name))/2)) + f_name + (" " * (len(f_name)%2)) + (" " * ((len(top) - 4 - len(f_name))/2)) + "**"
        else:
            print "**" + (" " * ((len(top) - 4 - len(f_name))/2)) + f_name + (" " * (len(top)%2)) + (" " * ((len(top) - 4 - len(f_name))/2)) + "**"
        print "**" + (" " * ((len(top) - 4 - len(l_name))/2)) + l_name + (" " * ((len(top) - 4 - len(l_name))/2)) + "**"
        print top
    elif len(f_name) > 6 and len(f_name) == len(l_name):
        top = "*" * (len(f_name) + 6)
        print top
        print "**" + (" " * ((len(top) - 10)/2)) + "Hello," + (" " * ((len(top) - 10)/2)) + "**"
        print "**" + (" " * ((len(top) - 4 - len(f_name))/2)) + f_name + (" " * ((len(top) - 4 - len(f_name))/2)) + "**"
        print "**" + (" " * ((len(top) - 4 - len(l_name))/2)) + l_name + (" " * (len(top)%2)) + (" " * ((len(top) - 4 - len(l_name))/2)) + "**"
        print top
    else:
        print "You messed up..."

greeting(f_name, l_name)