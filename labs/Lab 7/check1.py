"""
Function to parse a specific line format.

Author: Joe Noel (noelj)
"""

def parse_line(line):
    f = line.split("/", 3)
    if f[0].isdigit() == True and f[1].isdigit() == True and\
       f[2].isdigit() == True:
        return (int(f[0]),int(f[1]),int(f[2]),f[3])
    else:
        return None