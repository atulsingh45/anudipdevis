filename = "sample.txt"

count = 0

with open(filename, 'r') as file:
    for line in file:
        count += 1

print("Number of lines in the file:", count)
