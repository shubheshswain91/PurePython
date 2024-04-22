'''
Private member of parent class

We don’t always want the instance variables of the parent class to be inherited by the child class 
i.e. we can make some of the instance variables of the parent class private, which won’t be available to the child class. 

In Python inheritance, we can make an instance variable private by adding double underscores before its name. 

'''


class C():
    def __init__(self):
        self.c = 21

        # # d is private instance variable
        self.__d = 42

class D(C):
    def __init__(self):
        self.e = 111
        super().__init__()

obj = D()

print(obj.c)
print(obj.__d)