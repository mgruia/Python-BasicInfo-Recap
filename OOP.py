#classes and objects. Objects are instances of classes
class Person:
    pass

p = Person() #p is object of Person() class
#self = the current object you have

class Person:
    
    def getName(self):  # self = Person
        print("Asi")
    
    def getAge(self):
        print("37")
        
        
p = Person()
p.getName()
p.getAge()

# init allows us to create object of a class with specific properties

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        print("Your name is " + self.name)
    def getAge(self):
        print("Your age is " + self.age)
        
p1 = Person("Bob", "22")
p1.getAge()
p1.getName()
        