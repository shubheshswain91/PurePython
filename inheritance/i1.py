class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

p1 = Person("Ava", "Mills") 
p1.printname() 

''' Child class
To create a class that inherits the functionality from another class, 
send the parent class as a parameter when creating the child class

'''

class Student(Person):
#pass
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:



    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
            



'''
Use the super() Function
Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

'''

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("Mike", "Ola", 2019)

x.welcome()

