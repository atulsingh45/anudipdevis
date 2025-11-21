def simple_interest(P, R, T):
    SI = (P * R * T) / 100
    return SI

principal = float(input("Enter Principal amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time in years: "))

result = simple_interest(principal, rate, time)

print("Simple Interest =", result)
