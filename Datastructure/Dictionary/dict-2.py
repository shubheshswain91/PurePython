""" 
Sorting dictionary by values
 """


d1 = {'k1': 1, 'k2': 10, 'k3': 5,
       'k4': 2}
sorted_d1_asc1 = dict(sorted(d1.items(), key=lambda item: item[1]))       

""" 
Ascending order
 """

# Method 1
print(sorted_d1_asc1)


# Method 2

sorted_d1_asc2 = {k:v for k,v in sorted(d1.items(), key=lambda item: item[1])}

print(sorted_d1_asc2)


""" 
Descending order
 """

sorted_d1_desc1 = dict(sorted(d1.items(), key=lambda item: item[1], reverse=True))

print(sorted_d1_desc1)