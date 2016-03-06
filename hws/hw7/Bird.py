"""
Bird's class file.

Author: Joe Noel (noelj)
"""

import math
from Pig import *

class Bird(object):
    def __init__(self, info, time=0):
        self.name = info[0]
        self.x = float(info[1])
        self.y = float(info[2])
        self.radius = float(info[3])
        self.dx = float(info[4])
        self.dy = float(info[5])
        self.time = time
        self.alive = True
        
    def start(self):
        print "Time %d: %s starts at (%.1f,%.1f)"\
              %(self.time, self.name, self.x, self.y)
        
    def move(self): ##moves over one time increment
        self.x += self.dx
        self.y += self.dy
        
    def collision(self, pigs): ##check for collision
        i = 0
        rl = []
        for pig in pigs:
            distance = math.sqrt( (self.x-float(pig.x))**2 + (self.y-float(pig.y))**2 )
            if distance <= (self.radius + float(pig.radius)):
                print "Time %d: %s at (%.1f, %.1f) pops %s"\
                      %(self.time, self.name, self.x, self.y, pig.name)
                pig.pop()
                rl.append(i)
                self.dx *= 0.5
                print "Time %d: %s at (%.1f,%.1f) has (dx,dy) = (%.1f,%.1f)"\
                      %(self.time, self.name, self.x, self.y, self.dx, self.dy)
            i += 1
        for x in rl:
            del pigs[x]
                
    def check(self): ##checks speed and location
        speed = math.sqrt( self.dx**2 + self.dy**2 )
        if speed <= 6:
            print "Time %d: %s at location (%.1f,%.1f) with speed %.1f stops"\
                  %(self.time, self.name, self.x, self.y, speed)
            self.alive = False
        elif (self.x+self.radius) > 1000 or (self.y+self.radius) > 1000 or\
             (self.x-self.radius) < 0 or (self.y-self.radius) < 0:
            print "Time %d: %s at location (%.1f,%.1f) has left the game"\
                  %(self.time, self.name, self.x, self.y)
            self.alive = False
            