# Loop Through a Dictionary

thisdict = dict(name= "John", age = 36, country = "Sweden")
print(thisdict)

for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])   


for x in thisdict.values():
    print(x)

for x in thisdict.keys():
    print(x)

for x,y in thisdict.items():
    print(x,y)   

thisdict.clear()     