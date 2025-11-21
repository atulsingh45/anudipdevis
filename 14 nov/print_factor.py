num = int(input("Enter a number: "))

print("Factors of", num, "are:")

for i in range(1, num):
    if num % i == 0:
        print(i)
