"""
A program to calculate area and print the coinciding rectangle made of asteriks.

Author: Joe Noel (noelj)
"""

height = int(raw_input("Height==> "))
print height
width = int(raw_input("Width==> "))
print width

area = height * width

def burger(height, width):
    bun = "*" * width
    meat = "*" + (" " * (width-2)) + "*"
    side = (meat + "\n") * (height - 2)
    burger = bun + "\n" + side + bun
    print burger

def labeled_burger(height, width):
    bun = "*" * width
    label1 = "h: %d, w: %d" %(height, width)
    label2 = "area: " + str(area)
    meat = "*" + (" " * (width-2)) + "*"
    side = (meat + "\n") * (height - 2)
    if (len(label1) + 2) > width:
        burger(height, width)
        print "h: %d, w: %d" %(height, width)
        print "area: " + str(area)
    elif (len(label1) + 2) <= width:
        top_meat = (meat + "\n") * (height/2 - 2)
        ketchup = "*" + (" " * ((width - 2 - len(label1))/2)) + label1 + (" " * ((width - 2 - len(label1))/2)) + "*\n"
        mustard = "*" + (" " * ((width - 2 - len(label1))/2)) + label2 + (" " * ((width - 2)-((width - 2 - len(label1))/2)-len(label2))) + "*\n"
        bottom_meat = top_meat
        labeled_burger = bun + "\n" + top_meat + ketchup + mustard + bottom_meat + bun
        print labeled_burger

labeled_burger(height, width)
