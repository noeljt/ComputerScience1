"""
Determines whether there are enough legos or substitutes.

Author: Joe Noel (noelj)

"""

def lego_count(legos):
    size = raw_input("What type of lego do you need? ==> ")
    print size
    amount = int(raw_input("How many pieces of this lego do you need? ==> "))
    print amount
    if size == '1x1':
        if amount <= legos.count('1x1'):
            print "I have %d peices of 1x1 for this" %(legos.count('1x1'))
        else:
            print "I don't have enough pieces of this lego"
    elif size == '2x1':
        if amount <= legos.count('2x1'):
            print "I have %d pieces of 2x1 for this" %(legos.count('2x1'))
        elif amount <= (legos.count('1x1')/2):
            print "I have %d pieces of 1x1 for this" %(legos.count('1x1'))
        else:
            print "I don't have enough pieces of this lego"
    elif size == '2x2':
        if amount <= legos.count('2x2'):
            print "I have %d pieces of 2x2 for this" %(legos.count('2x2'))
        elif amount <= (legos.count('2x1')/2):
            print "I have %d pieces of 2x1 for this" %((amount*2))
        elif amount <= (legos.count('1x1')/4):
            print "I have %d pieces of 1x1 for this" %((amount*4))
        else:
            print "I don't have enough pieces of this lego"
    elif size == '2x4':
        if amount <= legos.count('2x4'):
            print "I have %d peices of 2x4 for this" %(legos.count('2x4'))
        elif amount <= (legos.count('2x2')/2):
            print "I have %d pieces of 2x2 for this" %((amount*2))
        elif amount <= (legos.count('2x1')/4):
            print "I have %d pieces of 2x1 for this" %((amount*4))
        elif amount <= (legos.count('1x1')/8):
            print "I have %d pieces of 1x1 for this" %((amount*8))
        else:
            print "I don't have enough pieces of this lego"

            
import hw3_util
legos = hw3_util.read_legos('legos.txt')

lego_count(legos)