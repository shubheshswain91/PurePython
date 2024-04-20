d = {'Raj': 10, 'Sam': 11, 'Tom': 30}
print(d.keys())
print(d.values())

d.update(Sami=33)

print(d)

del d['Raj']
print(d)

# to check whether a given key already exists in a dictionary.
def is_key_present(d, k):
    if k in d:
        print("present")
    else:
        print("Not present") 

is_key_present(d, "Sam")
is_key_present(d, "Bob")