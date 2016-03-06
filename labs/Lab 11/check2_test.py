"""
Test Cases:
-list of length 2
-duplicate values
-equidistant values
-list of ints
-list of floats
-list of both
-negative numbers
"""

import nose
from check2 import *

def test1():
    L1 = [4,8]
    (x,y) = closest2(L1)
    assert x == 4 and y == 8

def test2():
    L1 = [4,5,6,6,7,8,2,6]
    (x,y) = closest2(L1)
    assert x == 6 and y == 6

def test3():
    L1 = [3,4,5]
    (x,y) = closest2(L1)
    assert x == 3 and y == 4
    
def test4():
    L1 = [5,7,9,2,45,788,789]
    (x,y) = closest2(L1)
    assert x == 789 and y == 788
    
def test5():
    L1 = [3.5,4.6,5.1]
    (x,y) = closest2(L1)
    assert x == 5.1 and y == 4.6
    
def test6():
    L1 = [2,4,5.1,9.5]
    (x,y) = closest2(L1)
    assert x == 5.1 and y == 4
    
def test7():
    L1 = [5,-1,-2,8,34]
    (x,y) = closest2(L1)
    assert x == -2 and y == -1
    

if __name__ == '__main__':
    nose.runmodule()