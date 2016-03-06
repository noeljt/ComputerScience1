"""
A program to assist in scoring an olympic skater.

Author: Joe Noel (noelJ)
"""

j1_s = 21
j2_s = 32
j3_s = 28
j4_s = 24
j5_s = 29

j1_f = 24
j2_f = 28
j3_f = 19
j4_f = 23
j5_f = 24

def score(a,b,c,d,e):
    return a + b + c + d + e - max(a,b,c,d,e) - min(a,b,c,d,e)

def spread(a,b,c,d,e):
    average = score(a,b,c,d,e)/3.0
    return (float(max(a,b,c,d,e)) - min(a,b,c,d,e)) / average

def total_score(a,b,c,d,e,f,g,h,i,j):
    return int(score(a,b,c,d,e) + score(f,g,h,i,j))

print "Short program scores", j1_s, j2_s, j3_s, j4_s, j5_s
print "Free skating scores", j1_f, j2_f, j3_f, j4_f, j5_f
print "Spread of the short program is", spread(j1_s, j2_s, j3_s, j4_s, j5_s)
print "Spread of the free skating is", spread(j1_f, j2_f, j3_f, j4_f, j5_f)
print "Total score for the short program is", score(j1_s, j2_s, j3_s, j4_s, j5_s)
print "Total score for the free skating is", score(j1_f, j2_f, j3_f, j4_f, j5_f)
print "The total score for the competitor is", total_score(j1_s, j2_s, j3_s, j4_s, j5_s, j1_f, j2_f, j3_f, j4_f, j5_f)