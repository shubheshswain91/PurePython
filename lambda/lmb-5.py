""" 
Write a Python program to square and cube every number in a given list of integers using Lambda.

"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sq_lst = list(map(lambda x: x**2, lst))

print(sq_lst)

cube_lst = list(map(lambda x:x**3, lst))
print(cube_lst)
