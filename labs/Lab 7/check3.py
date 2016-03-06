"""
Program to find a given line within a given paragraph and file.

Author: Joe Noel (noelj)
"""

def parse_line(line):
    f = line.split("/", 3)
    if f[0].isdigit() == True and f[1].isdigit() == True and\
       f[2].isdigit() == True:
        return (str(f[0]),int(f[1]),int(f[2]),f[3])
    else:
        return None

def get_line(fname,parno,lineno):
    f = open(fname +'.txt')
    s = f.read()
    s2 = s.split("\n\n")
    p = s2[parno-1]
    lines = p.split("\n")
    return lines[lineno-1]+'\n'
    
def easter(fname,parno,lineno):
    f = open(fname+'.txt')
    program = open('program.txt','w')
    a = f.read()
    cut_text = a[a.find(get_line(fname,parno,lineno)):]
    lines = cut_text.split('\n')
    for line in lines:
        if parse_line(line) != None:
            f_line = line+'\n'
            break
    i = 0
    while i == 0:
        if parse_line(f_line)[0] == "0":
            break
        program.write(parse_line(f_line)[3])
        f2,p2,l2,code = parse_line(f_line)
        f_line = get_line(f2,p2,l2)
    program.close()
    
        
            

fname = raw_input('Please file number ==> ')
parno = int(raw_input('Please enter paragraph number ==> '))
lineno = int(raw_input('PLease enter the line number ==> '))

easter(fname,parno,lineno)