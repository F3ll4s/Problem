import math

class Calculator:
    def __init__(self,acc=0):
        self.acc = acc
    def set_accumulator(self,a):
        self.acc = a
    def get_accumulator(self):
        return self.acc
    def add(self,x):
        self.acc += x
    def subtract(self,x):
        self.acc -= x
    def multiply(self,x):
        self.acc *= x
    def divide(self,x):
        if x == 0:
            print("CANT DIVIDE BY ZERO")
        else:
            self.acc /= x
    def result(self,x):
        print(f"Result = {self.acc}")
        
class Sci_calc(Calculator):
    def __init__(self, acc=0):
        super().__init__(acc)
    def square(self):
        self.acc **= 2
    def exp(self,x):
        self.acc **= x
    def factorial(self):
        self.acc = math.factorial(self.acc)
        
    def print_result(self):
        print(f"Result: {format(self.acc,".2e")}")
    
x = Sci_calc(5)
x.factorial()
x.add(5)
x.divide(0)
x.print_result()