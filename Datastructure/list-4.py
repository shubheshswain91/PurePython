# Count the occurrence of each element from a list


#Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]





count_dict = dict()

for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1

    else:
        count_dict[item] = 1

print(count_dict)            
