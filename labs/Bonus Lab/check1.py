"""
Read file into a dictionary.

Author: Joe Noel (noelj)
"""

def read_file(file1):
    d = {}
    for line in open(file1):
        l = line.strip().split()
        s1 = set()
        for i in l[1:]:
            s1.add(int(i))
        d[int(l[0])] = s1
    return d

if __name__ == '__main__':
    file1 = raw_input('File ==> ')
    d = read_file(file1)
    print "%d people total" %(len(d))
    for key in d.keys():
        print "%d:" %(key), d[key]