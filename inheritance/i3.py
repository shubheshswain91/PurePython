# Parent class
class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name, self.idnumber)
        

# child class

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        self.sname = name
        self.idNummer = idnumber

        # invoking the __init__ of the parent class

        # Person.__init__(self, name, idnumber) 
        super().__init__("Rakesh", 2345)

    def displayInfo(self):
        print(self.sname, self.idNummer, self.salary, self.post)    

a = Employee("Raj", 1234, 3000, "Intern")

a.display()
a.displayInfo()