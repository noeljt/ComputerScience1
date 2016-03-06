"""
Calculates the Bunny and Fox population after 6 years.

Author: Joe Noel (noelj)
"""


def bpop_next(bpop, fpop):
    return (10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop

def fpop_next(bpop, fpop):
    return 0.4 * fpop + 0.02 * fpop * bpop

def pop_after6(bpop,fpop):
    print "INITIAL"
    print "Bunnies:", int(bpop), "Foxes:", int(fpop)
    print "AFTER 1 YEAR"
    bpop1 = int(bpop_next(bpop, fpop))
    fpop1 = int(fpop_next(bpop, fpop))
    print "Bunnies:", int(bpop1), "Foxes:", int(fpop1)
    print "AFTER 2 YEARS"
    bpop2 = int(bpop_next(bpop1, fpop1))
    fpop2 = int(fpop_next(bpop1, fpop1))
    print "Bunnies:", int(bpop2), "Foxes:", int(fpop2)   
    print "AFTER 3 YEARS"
    bpop3 = int(bpop_next(bpop2, fpop2))
    fpop3 = int(fpop_next(bpop2, fpop2))
    print "Bunnies:", int(bpop3), "Foxes:", int(fpop3)
    print "AFTER 4 YEARS"
    bpop4 = int(bpop_next(bpop3, fpop3))
    fpop4 = int(fpop_next(bpop3, fpop3))
    print "Bunnies:", int(bpop4), "Foxes:", int(fpop4)
    print "AFTER 5 YEARS"
    bpop5 = int(bpop_next(bpop4, fpop4))
    fpop5 = int(fpop_next(bpop4, fpop4))
    print "Bunnies:", int(bpop5), "Foxes:", int(fpop5) 
    print "AFTER 6 YEARS"
    bpop6 = int(bpop_next(bpop5, fpop5))
    fpop6 = int(fpop_next(bpop5, fpop5))
    print "Bunnies:", int(bpop6), "Foxes:", int(fpop6)

pop_after6(100,5)
pop_after6(100,18)