mystring = "this is a string"
print(mystring)
print(type(mystring))
print(mystring + " is the data type of " + str(type(mystring)))

firststring = "water"
secondstring = "fall"
thirdstring = firststring + secondstring
print(thirdstring)

name = input("what is your name?  ")
print(name)
color = input("what is favourite color?  ")
animal = input("what is favourite animal?  ")
print("your name is {}, your animal and color {} {}".format(name,animal,color))