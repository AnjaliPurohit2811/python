
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

while num2 != 0:
    temp = num2
    num2 = num1 % num2
    num1 = temp

gcd = num1

print("The GCD of", num1, "and", num2, "is:", gcd)
