# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

list1 = [54, 44, 27, 79, 91, 41]

element = list1.pop(4)

list1.insert(2, element)

list1.append(element)

print(list1)