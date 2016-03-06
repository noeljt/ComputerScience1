import lab06_util

bd = lab06_util.read_sudoku("solved.txt")
print bd

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
                
row = int(raw_input("row ==> "))
column = int(raw_input("column ==> "))
num = int(raw_input("number == >"))

okay_to_add(row,column,num)
print_board(bd)

#[['1', '4', '8', '6', '2', '9', '5', '3', '7'],\
 #['9', '6', '2', '7', '3', '5', '1', '4', '8'],\
 #['7', '5', '3', '4', '1', '8', '6', '2', '9'],\
 #['3', '2', '6', '9', '8', '7', '4', '5', '1'],\
 #['8', '9', '4', '1', '5', '3', '7', '6', '2'],\
 #['5', '7', '1', '2', '6', '4', '8', '9', '3'],\
 #['4', '3', '9', '8', '7', '6', '2', '1', '5'],\
 #['6', '1', '7', '5', '9', '2', '3', '8', '4'],\
 #['2', '8', '5', '3', '4', '1', '9', '7', '6']]