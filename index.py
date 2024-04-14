my_list = [1, 2, 3]


index = 0

try:
    value = my_list[index]
    print("Value at index {}: {}".format(index, value))
except IndexError:
    print("Error: Index out of range.")
