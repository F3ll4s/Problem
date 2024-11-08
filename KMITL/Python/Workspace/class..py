class Student:
    school = "KMITL"
    
    def __init__(self,name,personality,height):
        self.name = name
        self.personality = personality
        self.height = height
    @classmethod
    def getschool(cls):
        return cls.school
    def change(self,height2):
        self.height = height2
    def nigga():
        print("LOL")
        
        

James = Student("James","aggressive",159)
print(James.height)
James.change(125)
print(James.height)
print(Student.getschool())
Student.nigga()
