"""
Find two closest values in list and return tuple.

Author: Joe Noel (noelj)
"""

def closest1(L1):
    x0 = L1[0]
    y0 = L1[1]
    dif = abs(x0 - y0)
    i = 0
    for value1 in L1:
        n = 0
        for value2 in L1:
            if i == n:
                continue
            else:
                if abs(value1 - value2) < dif:
                    x0 = value1
                    y0 = value2
                    dif = abs(value1 - value2)
            n += 1
        i += 1
    return x0, y0

if __name__ == '__main__':
    L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
    (x,y) = closest1(L1)
    print x,y
                
                