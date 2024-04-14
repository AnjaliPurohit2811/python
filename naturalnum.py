range = int(input("Enter the range: "))
sum = 0
number = 1

while number <= range:
    sum += number
    number += 1

print("The sum of natural numbers up to", range, "is:", sum)
