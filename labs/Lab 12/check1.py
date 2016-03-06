def add(m,n):
    if n == 0:
        return m
    else:
        return add(m,n-1) + 1

def mult(m,n):
    if m == 0:
        return 0
    else:
        return add(n,mult(m-1,n))

def power(x,n):
    if n == 0:
        return 1
    else:
        return x * power(x,n-1)
    
if __name__ == '__main__':
    print add(5,3)
    print mult(8,3)
    print power(6,4)