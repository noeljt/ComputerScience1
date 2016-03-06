"""
A program to determine convergence points of bunny-fox populations.

Author: Joe Noel (noelj)
"""

def next_pop(bpop, fpop):
    bpop_next = max(0,int((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop))
    fpop_next = max(0,int(0.4 * fpop + 0.02 * fpop * bpop))
    return (bpop_next, fpop_next)

def check_convergence(bpop,fpop):
    i = 0
    bpop_i = bpop
    fpop_i = fpop
    history = [(bpop_i,fpop_i)]
    
    if bpop_i == 0 or fpop_i == 0:
        converge = True
        return (bpop, fpop, 1, converge)
    else:
        while i < 99:
            bpop,fpop = next_pop(bpop,fpop)
            history.append((bpop,fpop))
            if history[i] == history[i+1]:
                converge = True
                break
            elif bpop == 0 or fpop == 0:
                converge = True
                break
            elif i == 98:
                converge = False
                del history[-1]
                break
            i += 1
    return (bpop, fpop, (i+2), converge)

###############
## Main Code ##
###############

bpop_i = int(raw_input('Please enter the starting bunny population ==> '))
print bpop_i
fpop_i = int(raw_input('Please enter the starting fox population ==> '))
print fpop_i

(bpop, fpop, iterations, converged) = check_convergence(bpop_i,fpop_i)
    
print "(Bunny, Fox): Start " + str((bpop_i,fpop_i)) + " End: " +\
          str((bpop,fpop)) + ", Converged: " + str(converged) +\
          " in %d generations" %(iterations)
