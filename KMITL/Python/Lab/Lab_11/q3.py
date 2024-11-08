class Name:
    def __init__(self,x,y,z):
        self.title = x
        self.firstname = y
        self.lastname = z 
    def setName(self,t,f,l):
        self.title = t
        self.firstname = f
        self.lastname = l
    def getFullName(self):
        return f"{self.title}.{self.firstname} {self.lastname}"
    
class Date:
    def __init__(self,day,month,year):
        self.setDate(day,month,year)
    def setDate(self,d,m,y):
        if 1 <= d <= 31:
            self.day = d
        else:
            self.day = "error"
        if 1 <= m <= 12:
            self.month = m
        else:
            self.month = "error"
        self.year = y
    def getDate(self):
        return f"{self.day}/{self.month}/{self.year}"
    def getDateBC(self):
        self.BCyear = self.year + 543
        return f"{self.day}/{self.month}/{self.BCyear}"
    
class Address:
    def __init__(self,houseNo1,street1,district1,city1,country1,postcode1):
        self.houseNo = houseNo1
        self.street = street1
        self.district = district1
        self.city = city1
        self.country = country1
        self.postcode = postcode1
    def setAddress(self,houseNo,street,district,city,country,postcode):
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode
    def getAddress(self):
        return f"{self.houseNo},{self.street},{self.district},{self.city},{self.country},{self.postcode}"
    
class Department:
    def __init__(self,name,description,manager = ""):
        self.name = name
        self.description = description
        self.manager = manager
        self.employeeList = []
    def addEmployee(self,e):
        self.employeeList.append(e.name)
        e.department = self.name
    def deleteEmployee(self,e):
        self.employeeList.remove(e.name)
        self.description = "null"
    def setManager(self,e):
        self.manager = e
    def printinfo(self):
        print(f"Summary: {self.description}, Name : {self.name}, Manager: {self.manager}, Employee: {self.employeeList} ")
        
        
class Person:
    def __init__(self,name,birthdate,address):
        self.name = name.getFullName()
        self.birthdate = birthdate.getDate()
        self.address = address.getAddress()
    def printinfo(self):
        print(F"Name: {self.name}, Birthdate: {self.birthdate}, Address: {self.address}")
        
class Employee(Person):
    def __init__(self, name, birthdate, address,startdate,department = ""):
        super().__init__(name, birthdate, address)
        self.startdate = startdate
        self.department = department
    def printinfo(self):
        super().printinfo()
        print(f"StartDate: {self.startdate}, Department = {self.department}")
        
class TempEmployee(Employee):
    def __init__(self, name, birthdate, address, startdate, department,wage):
        super().__init__(name, birthdate, address, startdate, department)
        self.wage = wage
    def printinfo(self):
        super().printinfo()
        print(f"Wage: {self.wage}")
        
class PermEmployee(Employee):
    def __init__(self, name, birthdate, address, startdate, department,salary):
        super().__init__(name, birthdate, address, startdate, department)
        self.salary = salary
    def printinfo(self):
        super().printinfo()
        print(f"Salary: {self.salary}")
        
        
x = Name("Mr", "John", "Pork")
y = Date(15,6,2023)
addy = Address("45","Wok","45","Wok","45","Wok")

L = PermEmployee(x,y,addy,"15 Aug 2024","", 100)
L.printinfo()
cat = Department("Black","cat","Nigger")
cat.addEmployee(L)
cat.printinfo()
L.printinfo()

