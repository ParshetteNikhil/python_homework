value = int(input("enter the value - "))

count = 0
for x in range (2, (value //2 + 1)):
    if (value %x ==0):
        count = count + 1
    break
if (count ==0 and value !=1):
    print("%d is the prime number" %value)
else:
    print("%d is the composite number" %value)
