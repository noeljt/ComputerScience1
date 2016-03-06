
def closest2(L1):
    l = L1[:]
    l.sort()
    x0 = l[0]
    y0 = l[1]
    dif = abs(x0-y0)
    for i in range(2,len(l)):
        if abs(l[i]-l[i-1]) < dif:
            x0 = l[i]
            y0 = l[i-1]
            dif = abs(l[i]-l[i-1])
    return x0, y0
    
    
    
    
    
if __name__ == '__main__':
    L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
    (x,y) = closest2(L1)
    print x,y