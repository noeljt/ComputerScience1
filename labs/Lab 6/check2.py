"""
Program to check whether given number and placement is possible in soduku.

Author: Joe Noel (noelj)
"""


def okay_to_add(row,column,num):
    error = 0
    
    #check row
    i = 0
    for x in bd[row]:
        if i == column:
            i += 1
            continue
        else:
            i += 1
            if x == str(num):
                error += 1
    #check column
    for x in range(9):
        if x == row:
            continue
        else:
            if bd[x][column] == str(num):
                error += 1
    #check box
    if row <= 2 and column <= 2:
        n = 0
        for x in bd[:3]:
            i = 0
            for y in x[:3]:
                if i == column and n == row:
                    i += 1
                    continue
                elif y == str(num):
                    i += 1
                    error += 1
                else:
                    i += 1
            n += 1
    if row <= 2 and column > 2 and column <= 5:
        n = 0
        for x in bd[:3]:
            i = 3
            for y in x[3:6]:
                if i == column and n == row:
                    i += 1
                    continue
                elif y == str(num):
                    i += 1
                    error += 1
                else:
                    i += 1
            n += 1
    if row <= 2 and column > 5:
        n = 0
        for x in bd[:3]:
            i = 6
            for y in x[6:]:
                if n == row and i == column:
                    i += 1
                    continue
                elif y == str(num):
                    i += 1
                    error += 1
                else:
                    i += 1
            n += 1
    if row > 2 and row <= 5 and column <= 2:
        r = 3
        for x in bd[3:6]:
            c = 0
            for y in x[:3]:
                if r == row and c == column:
                    c += 1
                    continue
                elif y == str(num):
                    c += 1
                    error += 1
                else:
                    c += 1
            r += 1
    if row > 2 and row <= 5 and column > 2 and column <= 5:
        r = 3
        for x in bd[3:6]:
            c = 3
            for y in x[3:6]:
                if r == row and c == column:
                    c += 1
                    continue
                elif y == str(num):
                    c += 1
                    error += 1
                else:
                    c += 1
            r += 1
    if row > 2 and row <= 5 and column > 5:
        r = 3
        for x in bd[3:6]:
            c = 6
            for y in x[6:]:
                if r == row and c == column:
                    c += 1
                    continue
                elif y == str(num):
                    c += 1
                    error += 1
                else:
                    c += 1
            r += 1
    if row > 5 and column <= 2:
        r = 6
        for x in bd[6:]:
            c = 0
            for y in x[:3]:
                if r == row and c == column:
                    c += 1
                    continue
                elif y == str(num):
                    c += 1
                    error += 1
                else:
                    c += 1
            r += 1
    if row > 5 and column > 2 and column <= 5:
        r = 6
        for x in bd[6:]:
            c = 3
            for y in x[3:6]:
                if r== row and c == column:
                    c += 1
                    continue
                elif y == str(num):
                    c += 1
                    error += 1
                else:
                    c += 1
            r += 1
    if row > 5 and column > 5:
        r = 6
        for x in bd[6:]:
            c = 6
            for y in x[6:]:
                if r == row and c == column:
                    c += 1
                    continue
                elif y == str(num):
                    c += 1
                    error += 1
                else:
                    c += 1
            r += 1
    #all okay?
    if error > 0:
        print "This number cannot be added."
        return False
    else:
        bd[row][column] = num
        return True
        
def print_board(bd):
    print "-" * 25
    i = 0
    for x in bd:
        mystr = "|"
        n = 1
        
        for y in bd[i]:
            line = ""
            if (n%3) == 0 and n > 0 and n < 8:
                line = " |"
            mystr += " %s%s" %(y,line)
            n += 1
            
        i += 1
        print mystr + " |"
        if (i%3) == 0 and i > 0:
                print "-" * 25

###############
## Main Code ##
###############

bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

#print len(bd)
#print len(bd[0])
#print bd[0][0]
#print bd[8][8]

row = int(raw_input('Enter row number (0-8) ==> '))
column = int(raw_input('Enter column number (0-8) ==> '))
num = int(raw_input('Enter a number (1-9) ==> '))

okay_to_add(row, column, num)
print_board(bd)