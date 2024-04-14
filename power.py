def power(n,e):
    res=1
    for i in range(e):
        res *= n
    return res
print(power(4,2))