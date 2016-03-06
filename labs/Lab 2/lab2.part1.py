"""
A program to find total distance over a series of given coordinates.

Author: Joe Noel (noelj)
"""

## Function returns the length of a line 
## starting at (x1,y1) and ending at (x2,y2)
def line_length(x1,y1,x2,y2):
    length = (x1-x2)**2 + (y1-y2)**2
    length = length**(0.5)
    return length

total_line_length = line_length(100,100,100,160) + line_length(100,160,80,160) + line_length(80,160,90,120)
print total_line_length