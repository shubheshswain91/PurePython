# The dict() Constructor

thisdict = dict(name= "John", age = 36, country = "Sweden")
print(thisdict)


thisdict.pop("age")
print(thisdict)

thisdict.update({"city":"Berlin"})

print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["country"]
print(thisdict)

thisdict.clear()
print(thisdict)