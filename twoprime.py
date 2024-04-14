
start = int(input("Starting value: "))
end = int(input("ending value: "))

print("Prime numbers from", start, "to", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
 