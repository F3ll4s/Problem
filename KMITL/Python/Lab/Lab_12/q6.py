from abc import ABC, abstractmethod
from turtle import *


class TwoDShape(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def draw(self):
        pass
    
class Line(TwoDShape):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self):
        goto(self.x,self.y)
    
class Rectangle(TwoDShape):
    def __init__(self,x,y,length,width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
    def draw(self):
        penup()
        goto(self.x,self.y)
        pendown()
        for i in range(2):
            forward(self.length)
            left(90)
            forward(self.width)
            left(90)
    
class Circle(TwoDShape):
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
    def draw(self):
        penup()
        goto(self.x,self.y)
        pendown()
        circle(self.size)

class Square(TwoDShape):
    def __init__(self,x,y,length):
        self.x = x
        self.y = y
        self.length = length
    def draw(self):
        penup()
        goto(self.x,self.y)
        pendown()
        for i in range(4):
            forward(self.length)
            left(90)
    
    

meow = [Circle(100,200,30),Line(100,100),Rectangle(0,0,19,30),Square(30,30,50)]

for i in meow:
    i.draw()
done()