total=10
num1=0
num2=1
next=num2
inc=1
while inc<=total:
    inc+=1
    num1,num2=num2,next
    next=num1+num2
    print(next)