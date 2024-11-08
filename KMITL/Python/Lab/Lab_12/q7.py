from abc import ABC, abstractmethod
from turtle import *

class Transportation(ABC):
    @abstractmethod
    def __init__(self,x,y,z):
        self.start = x
        self.end = y
        self.distance = z
    
class Walk(Transportation):
    def __init__(self, x, y,z):
        super().__init__(x,y,z)
    def find_cost(self):
        return 0
        
class Taxi(Transportation):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
    def find_cost(self):
        return self.distance * 40
        
class Train(Transportation):
    def __init__(self, x, y, z,a):
        super().__init__(x, y, z)
        self.station = a
    def find_cost(self):
        return self.station * 5
    
meow = [Walk(100,200,0.6),Taxi(100,100,5),Train(0,0,40,6),Taxi(0,0,3)]
    
for i in meow:
    print(i.find_cost())
    