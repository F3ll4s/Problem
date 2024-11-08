class QuadraticEquation:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.discriminant = 0
        self.root1 = 0
        self.root2 = 0
    def getDiscriminant(self):
        self.discriminant = (self.b**2)-4*self.a*self.c
        return self.discriminant
    def getRoot1(self):
        if self.discriminant >= 0:
            self.root1 = (-self.b + (self.discriminant**0.5)) / (2*self.a)
            return self.root1
        else:
            return self.root1 == 0
    def getRoot2(self):
        if self.discriminant >= 0:
            self.root2 = (-self.b - (self.discriminant**0.5)) / (2*self.a)
            return self.root2
        else:
            return self.root2 == 0
        
t1 = QuadraticEquation(1,-8,5)
t1.getDiscriminant()
print(t1.discriminant)
t1.getRoot1()
t1.getRoot2()
print(t1.root1)
print(t1.root2)