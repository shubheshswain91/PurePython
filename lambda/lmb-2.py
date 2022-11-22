""" Write a Python program to create a function 
 that takes one argument, and that argument will 
 be multiplied with an unknown given number.
 """
"""  
print("Enter the number: ") 
num = int(input())


res = lambda x: x*num

print(res(num))
"""


def func_compute(n):
    return lambda x: x * n

res = func_compute(2)

print("Double the number of 15 =", res(15))

res = func_compute(3)

print("Triple the number of 15 =", res(15))