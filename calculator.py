num1=int(input("enter the value of num1="))
num2=int(input("enter the value of num2="))

print("press 1 for sum")
print("press 2 for sub")
print("press 3 for multiply")
print("press 4 for divison")
print("press 5 for module")
choice=int(input("enter your choice = "))

switcher(choice)
{
    1 : print("sum is=",num1+num2)
    2 : print("sub is=",num1-num2)
    3 : print("multiply is=",num1*num2)
    4 : print("divison is=",num1/num2)
    5 : print("module is=",num1%num2)
}