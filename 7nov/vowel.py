filename = "sample.txt"
vowels = 'aeiouAEIOU'
count = 0
with open(filename, 'r') as file:
    for line in file:
        for char in line:
            if char in vowels:
                count += 1

print("Number of vowels in the file:", count)
