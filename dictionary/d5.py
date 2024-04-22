# Nested Dictionaries

myfamily = {
    "child1" : {
        "name" : "Ana",
        "year" : 2004
    },

    "child2" : {
        "name" : "Bob",
        "year" : 2006
    },

    "child3" : {
        "name" : "Alex",
        "year" : 2009
    }
}

#print(myfamily)
#print(myfamily["child1"])
#print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
    print(x)

    for y in  obj:
        print(y + ':', obj[y])