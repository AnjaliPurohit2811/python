
n = int(input("Enter the numerator= "))
d = int(input("Enter the denominator= "))


try:
    result = n / d
    print("Result of division:", result)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
