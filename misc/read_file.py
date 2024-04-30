def read_file(myFile):
    with open(myFile, 'r') as file:
        lines = []
        for line in file:
            lines.append(line)
    return lines

content = read_file("misc/random.txt")
print(content)        