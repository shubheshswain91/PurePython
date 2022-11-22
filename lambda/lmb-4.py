""" 
Write a Python program to filter a list of integers using Lambda.

 """

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_lst = list(filter(lambda x: x%2 == 0, lst))

print(even_lst)

odd_lst = list(filter(lambda x: x%2 != 0, lst))

print(odd_lst)