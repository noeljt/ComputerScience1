"""
A program to fill in a madlibs.

Author: Joe Noel (noelj)
"""

name = raw_input("proper name==> ")
print name
emotion = raw_input("emotion==> ")
print emotion
verb = raw_input("verb==> ")
print verb
adjective = raw_input("adjective==> ")
print adjective
noun = raw_input("noun==> ")
print noun
adjective2 = raw_input("adjective==> ")
print adjective2
noun2 = raw_input("noun==> ")
print noun2
adjective3 = raw_input("adjective==> ")
print adjective3

print "Here is your output:"
print "Look, %s ...\n  I can see you're really %s about this ...\n  I honestly think you ought to %s calmly ...\n  take a %s %s and think things over ...\n  I know I've made some very %s decisions recently,\n  but I can give you my complete %s that my work will be back\n  to %s." %(name, emotion, verb, adjective, noun, adjective2, noun2, adjective3)