def read_file(myFile):
    with open(myFile, 'r') as file:
        for line in file:
            yield line

content = read_file("misc/random.txt")

print(content)  # Prints the Generator object

print(next(content))  # Prints the first line of the text file

print(next(content))  # Prints the second line  

print(next(content)) 

print(next(content)) 

"""
It yields one  item at a time instead of returning all items at once like list() does. This means that you can process each item individually 
without having to store them. When we get the first line, it gets deleted after fetching. To retrieve the first line we then have to call the read_file again.

"""
