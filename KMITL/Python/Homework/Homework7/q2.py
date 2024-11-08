class Poly:
    def __init__(self,value):
        self.value = value
    def add(self,value1):
        total =[]
        list0 = list(self.value)
        list1 = list(value1.value)
        length = 0
        if len(self.value) > len(value1.value):
            length = len(self.value) - len(value1.value)
            for i in range(length):
                list1.append(0)
        elif len(value1.value) > len(self.value):
            length = len(value1.value) - len(self.value)
            for i in range(length):
                list0.append(0)
        for i in range (len(list0)):
            cal = list0[i] + list1[i]
            total.append(cal)
        return Poly(tuple(total))
    def scalar_multiply(self,number):
        list = []
        for i in range (len(self.value)):
            num = self.value[i] * number
            list.append(num)
        return Poly(tuple(list))
    def multiply(self,value1):
        length = len(self.value) + len(value1.value) - 1
        new_list = [0] * length
        for i in range (len(self.value)):
            for j in range (len(value1.value)):
                new_list[i+j] += self.value[i] * value1.value[j]
        return Poly(tuple(new_list))
    def power(self,number):
        if number == 0:
            return Poly((1,))
        if number == 1:
            return self
        return self.multiply(self.power(number-1)) 
    def diff(self): 
        list = []
        for i in range(1,len(self.value)):
            value = self.value[i] * i
            list.append(value)
        return Poly(tuple(list))
    def integrate(self):
        list = []
        list.append(0)
        for i in range(len(self.value)):
            list.append(round(self.value[i]/(i+1),1))
        return Poly(tuple(list))
    def eval(self,number):
        total = 0
        for i in range (len(self.value)):
            total += self.value[i] * number ** i
        print(total)
        
    def print(self):
        for i in range (len(self.value)):
            if i == 0 :
                if self.value[i] > 0:
                    print(f"{self.value[i]}",end ="")
            else:
                if self.value[i] < 0:
                    value = abs(self.value[i])
                    print(f" - {value}x^{i}",end ="")
                elif self.value[i] == 0:
                    print(end="")
                elif self.value[0] == 0:
                    print(f"{self.value[i]}x^{i}",end ="")
                else:
                    print(f" + {self.value[i]}x^{i}",end ="")
            if i == len(self.value) - 1:
                print()
    
            
p = Poly((1,1,1,1))
q = Poly((1,1,1))
z = q.add(p).print()
z = q.scalar_multiply(5).print()
z = q.multiply(p).print()
z = q.power(2).print()
z = q.diff().print()
z = q.integrate().print()
z = q.eval(1)
