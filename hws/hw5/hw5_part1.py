"""
A program to take two paths and calculate position and distance.

Author: Joe Noel (noelJ)
"""

def walk(direction, (x,y) ):
    #changes coordinate based upon given direction
    if direction == "up":
        y += 1
    elif direction == "down":
        y -= 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1
    return (x,y)

def pathing():
    path1 = raw_input('Enter the first path ==> ')
    print path1
    path2 = raw_input('Enter the first path ==> ')
    print path2
    p1 = path1.split(",")
    p2 = path2.split(",")
    if len(p1) > len(p2):
        addition = "stay " * (len(p1)-len(p2))
        a = addition.split()
        p2 += a
    elif len(p2) > len(p1):
        addition = "stay " * (len(p2)-len(p1))
        a = addition.split()
        p1 += a
    n1 = p1[0]
    c1 = (int(p1[1]),int(p1[2]))
    n2 = p2[0]
    c2 = (int(p2[1]),int(p2[2]))
    di = abs(c1[0]-c2[0])+abs(c1[1]-c2[1])
    d_list = []
    d_list.append(di)
    print n1.capitalize().ljust(11) + "Action".ljust(11) +\
          n2.capitalize().ljust(11) + "Action".ljust(11) + "Distance".ljust(11)
    print str(c1).ljust(11) + "initial".ljust(11) + str(c2).ljust(11) +\
          "initial".ljust(11) + str(abs(c1[0]-c2[0])+abs(c1[1]-c2[1])).ljust(11)
    i = 3
    while i < len(p1):
        coor1 = walk(p1[i],c1)
        c1 = coor1
        coor2 = walk(p2[i],c2)
        c2 = coor2
        distance = abs(c1[0]-c2[0])+abs(c1[1]-c2[1])
        d_list.append(distance)
        print str(coor1).ljust(11) + p1[i].ljust(11) + str(coor2).ljust(11) +\
              p2[i].ljust(11) + str(distance).ljust(11)
        i += 1
    print "The minimum distance between them is %d" %(min(d_list))
    print "The maximum distance between them is %d" %(max(d_list))
    
pathing()