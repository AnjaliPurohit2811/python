def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

num = int(input("Enter the value =  "))
print("Sum of digits is = ", sum_of_digits(num))
