filename = "sample.txt"

count = 0

with open(filename, 'r') as file:
    for line in file:
        count += len(line)

print("Number of characters in the file:", count)
