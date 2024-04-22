# the __str__() function:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 34)

print(p1)

# The self parameter

class Derson:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print(f"Hello my name is {abc.name} and my age is {abc.age} ")

p2 = Derson("Vrek", 22)
p2.myfunc()  

p2.age = 23
p2.myfunc()

del p2.age
del p2