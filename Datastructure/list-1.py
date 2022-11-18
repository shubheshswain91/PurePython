# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 
# and even index elements from the list l2.


l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l3 = []

for idx, x in enumerate(l1):
    if idx%2 !=0:
        print(idx)
        l3.append(x)
        #print(x)
for idy, y in enumerate(l2):
    if idy%2 == 0:
        l3.append(y)


print(l3)
 #l3 = [x for x in l1 if x%2!=1]       
        
## second approach

res = list()

odd_elements = l1[1::2]

even_elements = l2[0::2]

res.extend(odd_elements)
res.extend(even_elements)

print(res)
