# Copy Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = thisdict.copy()

print(mydict)

# Make a copy of a dictionary with the dict() function:

dict_copy = dict(thisdict)
print(dict_copy)