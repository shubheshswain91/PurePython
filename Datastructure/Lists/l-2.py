""" 
Write a Python program to get the largest number from a list.

 """
lst = [1,6,2,0,-3]

max = 0
for item in lst:
    if item > max:
        max = item 

print(max)        