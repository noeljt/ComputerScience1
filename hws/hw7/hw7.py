"""
CS1 Angry Birds

Author: Joe Noel
"""

from Pig import *
from Bird import *


def make_list(file1, ind):
    f = file1.read().strip()
    f1 = f.split('\n')
    list1 = []
    if ind == 'Bird':
        for item in f1:
            x = item.split('|')
            y = Bird(x)
            list1.append(y)
    elif ind == 'Pig':
        for item in f1:
            x = item.split('|')
            y = Pig(x[0],x[1],x[2],x[3])
            list1.append(y)        
    return list1

def end_game(birds,pigs, ind):
    if len(pigs) == 0:
        if ind == 'p':
            print "Time %d: All pigs are popped. The birds win!" %(time)
            return True
        else:
            return True
    elif len(birds) == 0 and len(pigs) != 0:
        if ind == 'p':
            print "Time %d: No more birds. The pigs win!" %(time)
            print "Remaining pigs:"
            for pig in pigs:
                print pig.name
                return True    
        else:
            return True
    else:
        return False

if __name__ == '__main__':
    bird_f1 = raw_input("Enter the name of the birds file ==> ")
    print bird_f1
    bird_f = open(bird_f1)
    pig_f1 = raw_input("Enter the name of the pigs file ==> ")
    print pig_f1
    pig_f = open(pig_f1)
    birds = make_list(bird_f, 'Bird')
    pigs = make_list(pig_f, 'Pig')
    print "\nNum birds %d:" %(len(birds))
    for bird in birds:
        print "%s (%.1f,%.1f)" %(bird.name, bird.x, bird.y)
    print "."*4
    print "Num pigs %d:" %(len(pigs))
    for pig in pigs:
        print "%s (%.1f,%.1f)" %(pig.name, float(pig.x), float(pig.y))
    print "."*4
    time = 0
    while end_game(birds,pigs, 'p') == False:
        i = 0
        rl = []
        for bird in birds:
            bird.time = time
            bird.start()
            while bird.alive == True and end_game(birds,pigs, 'n') == False:
                time += 1
                bird.time = time
                bird.move()
                bird.collision(pigs)
                bird.check()
            rl.append(i)
            i += 1
        rl.sort(reverse=True)
        for i in rl:
            del birds[i]
        
                
                
                