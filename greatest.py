a = int(input("enter the number -1 "))
b = int(input("enter the number -2 "))
c = int(input("enter the number -3 "))

if (a > b) and (a > c):
    print("number -1 is greater than number -2 & number -3")
elif (b > a) and (b > c):
    print("number -2 is greater than number -1 & number -3")
else:
    print("number -3 is greater than number -1 & number -2")

