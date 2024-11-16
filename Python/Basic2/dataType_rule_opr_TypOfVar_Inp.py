# a = 21
# b = 22
# print(a+b)


# datatype in python------------------------------------------------------------------------>>>

a = 21  # a is an integer
b = 2.22 # b is a floating point number
c = "Akram" # c is a string variable
d = False # d is a boolean variable
e = True # e is a boolean variable
f = None # f is a none type variable


# rules of defining the variables------------------------------------------------------------>>>

# @akram = 33 #invalid variable
_Akram = "men" #valid variable
Akram_ = "akram" # valid variable
# 0akram = "string" #invalid variable
# Akram@ = "Akkku" # invalid variable



# Operators ----------------------------------------------------------------------------------->>>
# Arithmetic operator
# a = 3
# b = 4
# c = a + b
# print (c)

# Assignment operator
# a = 4-3
# print(a)

# b = 6
# b += 4    # increment
# print(b)

# b -= 3    # decrement
# print(b)

# b /= 3 # divide
# print(b)

# Comparison operator
# d = 6<3          # false
# print(d)

# d = 6>=3           # true
# print(d)

# d = 5!=3           # true
# print(d)

# d = 4!=4           # false
# print(d)

# Logical Operators
e = True or False
# print(e)

# Truth table of "or"
# print("True or False :=", True or False)
# print("True or True :=", True or True)
# print("False or False :=", False or False)
# print("False or True :=", False or False)

# Truth Table of "and"
# print("True and False :=", True and False)
# print("True and True :=", True and True)
# print("False and False :=", False and False)
# print("False and True :=", False and False)

# Truth table of not
# print(not(False)) # true
# print(not(True)) # false



# Type of Variable----------------------------------------------------------------------------->>>
a = 31.5
t = type(a)  #<class 'float'>
# print(t)

b = 33
t = type(b)  #<class 'integer'>
# print(t)

c = False
t = type(c) #<class 'boolean'>
# print(t)

d = "Akram"
t = type(d) #<class 'string'>
# print(t)


# type conversion, one datatype to another datatype
e = "3.2"
f = float(e) # e but the type should be float / type conversion
t = type(f)  #<class 'float'>
# print(t)



#input-------------------------------------------------------------------------------------->>>
# a = input("Enter the one number: ")
# b = input("Enter the two number: ")

# print("Number a is: ", a)
# print("Number b is: ", b)

# print("Addition of a & b is: ",(a + b)) # result is 5566, bez of a and b is taking a string input that's why, also called string concatenation
# print("substraction of a & b is: ", a - b) #TypeError: unsupported operand type(s) for -: 'str' and 'str', bcz both are strings


# input type conversion---------------------------------------------------------------------->>>>>

a = int(input("Enter the one number: "))
b = int(input("Enter the two number: "))

print("Number a is: ", a)
print("Number b is: ", b)
print("Sum of a & b is: ", (a + b))