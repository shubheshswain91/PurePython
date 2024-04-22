'''
Protetcted member
Protected members (in C++ and JAVA) are those members of the class that cannot be accessed outside the class 
but can be accessed from within the class and its subclasses. To accomplish this in Python, 
just follow the convention by prefixing the name of the member by a single underscore “_”.

'''

class Base:
    def __init__(self):
        self._a = 2

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class: ", self._a)


        # Modify the protected variable:
        self._a = 3
        print("Calling modified protected member outside class: ", self._a)



obj1 = Derived()

obj2 = Base()

# Calling protected member 
# Can be accessed but should not be done due to convention 
print("Accessing protected member of obj1: ", obj1._a) 
  
# Accessing the protected variable outside 
print("Accessing protected member of obj2: ", obj2._a) 
