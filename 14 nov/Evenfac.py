def even_factors(n):
    print("Even factors of", n, "are:")
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 0:   # i is a factor AND i is even
            print(i)

num = int(input("Enter a number: "))
even_factors(num)