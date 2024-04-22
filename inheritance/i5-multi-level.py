'''
Multilevel inheritance: When we have a child and grandchild
relationship. This means that a child class will inherit 
from its parent class, which in turn is inheriting 
from its parent class.
'''

class Base():
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

class Child(Base):
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    def getAge(self):
        return self.age

class GrandChild(Child):
    def __init__(self, name, age, address):
        Child.__init__(self, name, age) 
        self.address = address

    def getAddress(self):
        return self.address

g = GrandChild("Geek1", 23, "Bombay")

print(g.getName(), g.getAge(), g.getAddress())
