"""
Sorting Method 1:
O(N^2)

Sorting Method 2:
O(Nlog(N)+N)
"""

from check1 import *
from check2 import *
import time
import random

if __name__ == '__main__':
    maxrange = 1000
    L = []
    for i in range(maxrange):
        L.append(random.uniform(0.0,1000.0))
    
    start = time.time()
    (x,y) = closest1(L)
    end = time.time()
    print "Sorting method 1 took", end-start
    
    start = time.time()
    (x,y) = closest2(L)
    end = time.time()
    print "Sorting method 2 took", end-start
    