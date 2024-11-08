from abc import ABC, abstractmethod
from turtle import *

class Char(ABC):
    @abstractmethod
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
class Char0(Char):
    def __init__(self, x, y):
        super().__init__(x, y)
    def draw(self):
        penup()
    def getWidth(self):
        return self.width
    
class Char1(Char):
    def __init__(self, x, y):
        super().__init__(x, y)
    def draw(self):
        penup()
        goto(self.x,self.y)
        pendown()
        right(90)
        forward(25)
        right(180)
        forward(50)
        left(135)
        forward(17.5)
    def getWidth(self):
        return self.width

class Char2(Char):
    def __init__(self, x, y):
        super().__init__(x, y)
    def draw(self):
        penup()
        goto(self.x,self.y)
        
        
    def getWidth(self):
        return self.width

    
x = [Char0(20,50),Char1(0,0)]

for i in x:
    i.draw()
exitonclick()