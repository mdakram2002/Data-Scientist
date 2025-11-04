

# num1 = int(input("Enter the value of A: "))
# num2 = int(input("Enter the value of B: "))


# print(f"it is formatted string style{num1} and {num2}")
# if (num1 > num2):
#     print(f"{num1} is greater then {num2}")

# elif num2 > num1:
#     print(f"{num2} is greater then the {num1}")

# else:
#     print(f"Now, {num2} is equal to {num1}")


# gen = input("Please tell your gender as character (M or F): ")

# if gen == 'M' or gen == 'm':
#     print(f"Yes, my gender is {gen}: ")

# elif gen == 'F' or gen == 'f':
#     print(f"Yes, my gender is {gen}: ")

# else:
#     print(f"Sorry, I can't tell you my gender")

# name = input("Enter your name")
# age = int(input("Enter your age"))

# if age >= 18:
#     print(f"Hello {name} you are a valid voter")

# else:
#     print(f"Hello {name} you are not a valid voter")


# for loop

# for i  in range(1, 21, 1):
# for i  in range(21):  # by default it's start from 0;


# for i  in range(21, 51):
#     print(i)

# for i  in range(21, 1, -1): # Here start from 1 and go back or nigative
#     print(i)


# for i  in range(-5, -16, -1):
    # print(i)

# for i in range(5, 51 , 5): # Here start from 5, to 51 because we want 50, and steps is 5
#     print(i)

# n = int(input("Which table you want? "))

# for i in range(n, (n*10) + 1, n):
#     print(i)



# STRING WITH LOOP
a  = "AKRAMSHAIKH  FROM BIHAR"

# print(len(a))

# for i in range(len(a)):
#     print(a[i])

# for i in a:
#     print(i)

# for i in range(1, 21):
#     if i == 15:
#         break
#     else:
#         print(i)


# for i in range(1, 21):
#     if i == 15:
#         continue
#     print(i)


# for i in range(1, 21):
#     if i == 61:
#         print("Break statement is executed")
#         break
#     print(i)

# else:
#     print("Break statement is not executed")


# n = int(input("Please tell your number: "))

# for i in range(n):
#     print("Hello, Akram Kese ho")



# n = int(input("Please tell your number: "))

# for i in range(1, n+1):
#     print(f"Here is that number as you want to print: {i}")



# n = int(input("Please tell your number: "))

# for i in range(n, 0 ):
#     print(f"Here is that number as you want to print: {i}")



# n = int(input("which table you want to read: "))

# for i in range(1, 11):
#     print(f"{n} * {i} = {n * i}") # THIS IS FORMATTED STRING APPROACH


# n = int(input("Enter your number: "))
# sum = 0

# for i in range(1, n + 1):
#     sum = sum + i

# print(f"you sum is {sum}")


# FACTORIAL NUMBER
# n = int(input("Enter your num: "))
# fact = 1

# for i in range(1, n+1):
#     fact = fact * i

# print(f"Your FACTORIAL IS: {fact}")



# EVEN AND ODD OF SUM
# n = int(input("Enter your number: "))
# even = 0
# odd = 0

# for i in range(1, n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i

# print(f"Your EVEN AND ODD OF SUM: {even} and {odd}")



# FACTOR OF INTEGER
# n = int(input("Enter you number as you want to factor: "))

# for i in range(1, n+1):
#     if n%i == 0:
#         print(i)



# CHECK NUMBER IS PERFECT OR NOT
# n = int(input("Enter your that you want to check is it Perfect number: "))
# sum = 0

# for i in range(1, n):
#     if n%i == 0:
#         sum = sum + i

# if sum == n:
#     print("Your number is perfect")
# else:
#     print("not a perfect")



# CHECK PRIME NUMBER
# n = int(input("Check the number is prime or not: "))

# count = 0
# for i in range(1, n + 1):
#     if n%i == 0:
#         count = count + 1

# if count == 2:
#     print("your number is prime")
# else:
#     print("your number is not prime")



# REVERSE A STRING
# a = "AKRAM SHAIKH"

# # print(a[::-1])
# #  start lecture here:= 3:29:34

# b = ""
# for i in range(len(a)-1, -1, -1):
#     b = b + a[i]
# print(b)


# CHECK STRING IS PALINDROM
# a = input("Check string is palindrom or not: ")
# b = ""

# for i in range(len(a)-1, -1, -1):
#     b = b + a[i]

# if b == a:
#     print("Your string is palindrom")
# else:
#     print("yout string is not a palindrom")



# MATHODS OF STRING
# a = "akram@$*^$:323425;?/^&*(_+)"
# char = 0
# dig = 0
# spchr = 0

# for i in a:
#     if i.isdigit():
#         dig +=1
#     elif i.isalpha():
#         char +=1
#     else:
#         spchr +=1

# print(f"Your digits are are: {dig}\nyour alphabates are: {char}\nyour special charactor are: {spchr}")


print(dir(str))