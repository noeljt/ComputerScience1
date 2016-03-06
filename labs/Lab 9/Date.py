'''
Start to the Date class for Lab 10.  This code will not run in Python
until three methods are added:
    __init__,
    __str__
    same_day_in_year
'''

days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',\
                    'September', 'October', 'November', 'December' ]

class Date(object):
    def __init__(self, year=1900, month=1, day=1):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        
    def __str__(self):
        return "%d/%s/%s" \
               %(self.year,str(self.month).rjust(2,'0'),str(self.day).rjust(2,'0'))
    
    def same_day_in_year(self, other):
        return self.month == other.month and self.day == other.day
    
    def is_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    
    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                if self.day < other.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

if __name__ == "__main__":
    
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1996, 4, 13)
    print "d1: " + str(d1)
    print "d2: " + str(d2)
    print "d3: " + str(d3)
    print "d1.same_day_in_year(d2)", d1.same_day_in_year(d2) 
    print "d2.same_day_in_year(d3)", d2.same_day_in_year(d3)
    
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1998, 5, 13)
    d4 = Date(1998, 4, 11)
    print d1 < d2
    print d2 < d3
    print d3 < d4
    
    d1 = Date(2000)
    d2 = Date(2004)
    d3 = Date(1900)
    d4 = Date(2002)
    print d1.is_leap_year()
    print d2.is_leap_year()
    print d3.is_leap_year()
    print d4.is_leap_year()
    
    d5 = Date()
    print str(d5)