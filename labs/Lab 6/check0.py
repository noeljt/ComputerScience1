"""
Author: Joe Noel (noelj)
"""

#list counting from 0 to 8
i = 0
list1 = []
while i <= 8:
    list1.append(i)
    i += 1
print list1

#list of rows
row = 0
rows = []
while row <= 8:
    column = []
    for x in list1:
        column.append( (row,x) )
    rows.append(column)
    row += 1

print rows

#print rows
row = 0
print board[row]

#prints given column
i = 0
column = 0
colist = []
while i <= 8:
    colist.append(board[i][column])
    i += 1
print colist