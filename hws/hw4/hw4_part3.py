"""
Horror Movie Stuff.

Author: Joe Noel (noelj)
"""

def block(s, length):
    sen = list(s)
    sen.append(" ")
    mystr = ""
    line = []
    n = 0
    while n < (length*10):
        line.append(n)
        n += 1
    while (mystr.count("\n")) < 9:
        for x in line:
            if (x+1) < len(sen) and (x+1)%length != 0:
                mystr += sen[x]
            elif (x+1) >= len(sen) and (x+1)%length != 0:
                mystr += sen[(x)-len(sen)*(x/len(sen))]
            elif (x+1)%length == 0:
                mystr += sen[(x)-len(sen)*(x/len(sen))] + "\n" 
    print mystr

###############
## Main Code ##
###############

s = raw_input('Please enter a line ==> ')
print s
length = int(raw_input('Please enter a line length ==> '))
print length

block(s, length)