"""
Program to check whether given number and placement is possible in soduku.

Author: Joe Noel (noelj)
"""


def ok_to_add(row, column, num):
    
    error = 0
    #row okay?
    for x in bd[0:row]:
        if str(num) == x:
            error += 1
    for x in bd[row+1:]:
        if str(num) == x:
            error += 1
    #column okay?
    i = 0
    while i <= 8:
        if i == num:
            print "cont"
            i += 1
            continue
        if bd[i][column] == str(num):
            error += 1
        i += 1
    #box okay?
    if row <= 2 and column <= 2:
        for x in bd[:3]:
            for y in x[0:column]:
                if y == str(num):
                    error += 1
            for y in x[column+1:3]:
                if y == str(num):
                    error += 1
    if row <= 2 and column > 2 and column <= 5:
        for x in bd[:3]:
            for y in x[3:column]:
                if y == str(num):
                    error += 1
            for y in x[colum+1:6]:
                if y == str(num):
                    error += 1
    if row <= 2 and column > 5:
        for x in bd[:3]:
            for y in x[6:column]:
                if y == str(num):
                    error += 1
            for y in x[colum+1:]:
                if y == str(num):
                    error += 1            
    if row > 2 and row <= 5 and column <= 2:
        for x in bd[3:6]:
            for y in x[0:column]:
                if y == str(num):
                    error += 1
            for y in x[column+1:3]:
                if y == str(num):
                    error += 1
    if row > 2 and row <= 5 and column > 2 and column <= 5:
        for x in bd[3:6]:
            for y in x[3:column]:
                if y == str(num):
                    error += 1
            for y in x[column+1:6]:
                if y == str(num):
                    error += 1
    if row > 2 and row <= 5 and column > 5:
        for x in bd[3:6]:
            for y in x[6:column]:
                if y == str(num):
                    error += 1
            for y in x[column+1:]:
                if y == str(num):
                    error += 1
    if row > 5 and column <= 2:
        for x in bd[6:]:
            for y in x[:column]:
                if y == str(num):
                    error += 1
            for y in x[column+1:3]:
                if y == str(num):
                    error += 1
    if row > 5 and column > 2 and column <= 5:
        for x in bd[6:]:
            for y in x[3:column]:
                if y == str(num):
                    error += 1
            for y in x[column+1:6]:
                if y == str(num):
                    error += 1
    if row > 5 and column > 5:
        for x in bd[6:]:
            for y in x[6:column]:
                if y == str(num):
                    error += 1   
            for y in x[column+1:]:
                if y == str(num):
                    error += 1
    #all okay?
    if error > 0:
        print "This number cannot be added."
    else:
        bd[row][column] = num

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

ok_to_add(row, column, num)

#prints the board
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
            
