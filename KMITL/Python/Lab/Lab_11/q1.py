class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def printinfo(self):
        print(f"Point: ({self.x}, {self.y})")
        
class Circle(Point):
    def __init__(self, x=0, y=0,r=0):
        super().__init__(x, y)
        self.radius = r
    def area(self):
        return 3.14 * self.radius * self.radius 
    def printinfo(self):
        super().printinfo()
        print(f"Radius: {self.radius}")
        print(f"Area: {self.area()}")
        
x = Circle(2,3,4)
x.printinfo()