"""
Program to find a given line within a given paragraph and file.

Author: Joe Noel (noelj)
"""

def parse_line(line):
    f = line.split("/", 3)
    print f
    if f[0].isdigit() == True and f[1].isdigit() == True and\
       f[2].isdigit() == True:
        return (int(f[0]),int(f[1]),int(f[2]),f[3])
    else:
        return None

def get_line(fname,parno,lineno):
    f = open(fname +'.txt')
    s = f.read()
    s2 = s.split("\n\n")
    p = s2[parno-1]
    lines = p.split("\n")
    return lines[lineno-1]+'\n'
    

fname = raw_input('Please file number ==> ')
parno = int(raw_input('Please enter paragraph number ==> '))
lineno = int(raw_input('PLease enter the line number ==> '))

print get_line(fname,parno,lineno)