# Import the Counter class from the collections module
from collections import Counter

# Create a Counter object 'c' with specified initial counts for keys 'p', 'q', 'r', and 's'
c = Counter(p=4, q=2, r=0, s=-2)

# Print the elements in the Counter 'c' as a list
print(list(c.elements())) 