class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d 
        self.__e = e
        self.__f = f
    def getA(self):
        return self.__a
    def getB(self):
        return self.__b
    def getC(self):
        return self.__c
    def getD(self):
        return self.__d
    def getE(self):
        return self.__e
    def getF(self):
        return self.__f
    def isSolvable(self):
        if (self.getA() * self.getD()) - (self.getB() * self.getC()) != 0:
            return True
        else:
            return False
    def getX(self):
        if self.isSolvable() == True:
            return (self.getE() * self.getD()) - (self.getB()*self.getF()) / (self.getA() * self.getD()) - (self.getB() * self.getC())
    def getY(self):
        if self.isSolvable() == True:
            return (self.getA()*self.getF()) - (self.getE()*self.getC())/ (self.getA() * self.getD()) - (self.getB() * self.getC())
        
p = LinearEquation(1,2,3,4,5,6)
print(p.getX())
print(p.getY())