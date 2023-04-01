value = int(input(" Please enter value - "))
count = 1

for x in range(1, value + 1):
    count = count * x
print("The factorial of %d  = %d" %(value, count))
