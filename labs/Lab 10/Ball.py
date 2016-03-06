
class Ball(object):
    def __init__(self, x, y, dx, dy, r, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = r
        self.color = color
        
    def position(self):
        return (self.x,self.y)
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
    
    def bounding_box(self):
        return (self.x-self.radius, self.y-self.radius,\
                self.x+self.radius, self.y+self.radius)
    
    def get_color(self):
        return self.color
    
    def some_inside(self, maxx, maxy):
        return self.x > maxx and self.y > maxy
    
    def check_and_reverse(self, maxx, maxy):
        if self.x + self.radius >= maxx or self.x - self.radius <= 0:
            self.dx *= -1
        if self.y + self.radius >= maxy or self.y - self.radius <= 0:
            self.dy *= -1