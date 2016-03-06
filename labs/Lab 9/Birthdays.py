
from Date import *

def get_bdays(file1):
    f = open(file1).read().strip().split('\n')
    listB = []
    for bday in f:
        temp = bday.split()
        listB.append(Date(temp[0],temp[1],temp[2]))
    return listB
    

if __name__ == '__main__':
    bdays = get_bdays('birthdays.txt')
    oldest = Date()
    youngest = Date()
    i = 1
    while i < len(bdays):
        if i == 1:
            if bdays[i] < bdays[i-1]:
                oldest = bdays[i]
                youngest = bdays[i-1]
            elif bdays[i-1] < bdays[i]:
                oldest = bdays[i-1]
                youngest = bdays[i]
        else:
            if bdays[i] < oldest:
                oldest = bdays[i]
            elif youngest < bdays[i]:
                youngest = bdays[i]            
        i += 1
    del month_names[0]
    m_l = []
    for month in month_names:
        m_l.append( [month, 0] )
    for bday in bdays:
        m_l[bday.month-1][1] += 1
    i = 0
    for month in m_l:
        if i == 0:
            most_bdays = month
        else:
            if month[1] > most_bdays[1]:
                most_bdays = month
        i += 1
        
    print str(oldest)
    print str(youngest)
    print most_bdays[0]