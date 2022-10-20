#class inheritance
#child class inherits all the properties and functions of the parent class

class Parent:
    def __init__(self):
        print("This is the parent class")
    def parentFunc(self):
        print("This is the parent function")
        
p = Parent() #call the parent class
p.parentFunc() #call the parent function

class Child(Parent): #child inherits parent
    def __init__(self):
        print("This is the child class")
    def childFunc(self):
        print("This is the child function")
        
c = Child()
c.childFunc()
c.parentFunc()

#how to override methods
class Parent:
    def __init__(self):
        pass
    def test(self):
        print("parent")

p = Parent()
p.test()