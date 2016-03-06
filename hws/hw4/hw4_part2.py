"""
A program to compare countries to the United states medal contribution.

Author: Joe Noel (noelj)
"""

#gets total numbers for all medals and each specific medal
def totals(medals):
    total_g = 0
    total_s = 0
    total_b = 0
    total = 0
    i = 0
    while i < len(medals):
        total_g += medals[i][1]
        total_s += medals[i][2]
        total_b += medals[i][3]
        total += medals[i][4]
        i += 1
    totals = [total_g, total_s, total_b, total]
    return totals

#prints statstics line
def percentages(year, medals, totals, country):
    i = 0
    stats = [0,0,0,0,0]
    while i < len(medals):
        for x in medals[i]:
            if medals[i][0].lower() == country.lower():
                stats = medals[i]
        i += 1
    goldp = str(int((stats[1]/float(totals[0])*100))) + "%"
    silvp = str(int((stats[2]/float(totals[1])*100))) + "%"
    bronp = str(int((stats[3]/float(totals[2])*100))) + "%"
    totap = str(int((stats[4]/float(totals[3])*100))) + "%"
    if stats[4] != 0:
        print year.ljust(8) + country.capitalize().ljust(14) + goldp.rjust(8) +\
              silvp.rjust(8) + bronp.rjust(8) + totap.rjust(8)

#puts it all together...
def olympics(country):
    print "Year".ljust(8) + "Country".ljust(14) + "Gold".rjust(8) +\
          "Silver".rjust(8) + "Bronze".rjust(8) + "Total".rjust(8)
    print "=" * 54
    percentages('2010', medals2010, totals2010, country)
    percentages('2010', medals2010, totals2010, 'United States')
    print ""
    percentages('2014', medals2014, totals2014, country)
    percentages('2014', medals2014, totals2014, "United States")

###############
## Main Code ##
###############

import hw4_util
medals2010 = hw4_util.read_medals('medals2010.txt')
medals2014 = hw4_util.read_medals('medals2014.txt')    
    
country = raw_input('Enter the name of a country ==> ')
print country
totals2010 = totals(medals2010)
totals2014 = totals(medals2014)
olympics(country)