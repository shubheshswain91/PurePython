""" 
Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings

 """
lst = ['abc', 'xyz', 'aba', '1221']

length = 0
for item in lst:
    #length = len(item)
    #print(length)
    if item[0] == item[-1]:
        print('same')
    else:
        print("not same")    