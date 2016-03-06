"""
Program to check whether given number and placement is possible in sudoku.

Author: Joe Noel (noelj)
"""

#prints the board
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
          
#determines whether board is solved
def verify_board(board):
    i = 0
    t_f = 0
    while i <= 8:
        for x in board[i]:
            if x == ".":
                t_f += 1
        i += 1
    
    i = 0
    list1 = [0,1,2,3,4,5,6,7,8]
    while i <= 8:
        for y in list1:
            if okay_to_add_v(i,y,board[i][y]) == False:
                t_f += 1
        i += 1
    
    
    if t_f == 0:
        print "Board is solved!"
        return True
    else:
        return False
            
#determines whether a number can be added to a position (w/o print)
def okay_to_add_v(row,column,num):
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
        return False
    else:
        bd[row][column] = num
        return True

#determines whether a number can be added to a position
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
    else:
        bd[row][column] = num
    
###############
## Main Code ##
###############

import lab06_util

bd = lab06_util.read_sudoku(raw_input('file name? ==> '))
print bd

while verify_board(bd) == False:
    print_board(bd)
    row = int(raw_input("Row ==> "))
    column = int(raw_input("Column ==> "))
    num = int(raw_input("Number ==> "))
    okay_to_add(row,column,num)
    
    