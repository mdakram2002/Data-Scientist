
x = int(input("Enter your age: "))

if(x>18):
    print("You are above the age of consent")

else:
    print("You are below the age of consent")


# if elif else
if(x>18):
    print("You are above the age of consent")

elif(x<0):
    print("You are entering an invalid age")

else:
    print("You are below the age of consent")


# Problem 01
# taking input as int and type as string
a1 = int(input("ENter num 1: "))
a2 = int(input("ENter num 2: "))
a3 = int(input("ENter num 3: "))
a4 = int(input("ENter num 4: "))


if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1: ", a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a2: ", a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is a3: ", a3)

elif(a4>a1 and a4>a2 and a4>a3):
    print("Greatest number is a4: ", a4)


# problem 02

marks = int(input("Enter Your marks: "))
if(marks > 40):
    print("Congratulation, You are pass for all subjects")

elif(marks < 40):
    print("Faild for any one subject ")

else:
    print("you are not apair in examination")



# problem 3, 12th pass and fail with percentage.
marks1 = int(input("Enter Your marks of Physics: "))
marks2 = int(input("Enter Your marks of Chemistry: "))
marks3 = int(input("Enter Your marks of Mathematics: "))
marks4 = int(input("Enter Your marks of English: "))
marks5 = int(input("Enter Your marks of Urdu: "))

total_percentage = (100 *(marks1 + marks2 + marks3 + marks4 + marks5))/500

if(total_percentage >= 40):
    print("Congratulation, You are pass for all subjects and you got:", total_percentage,"% marks")

else:
    print("You Failed, try again next year and you got:", total_percentage,"% marks")


# Q No. 4: Write a program calculate total percentage of all subjects with 40
# 5 and atlest in one subject marks shuld be grater then 33.

marks1 = int(input("Enter Your marks of Physics: "))
marks2 = int(input("Enter Your marks of Chemistry: "))
marks3 = int(input("Enter Your marks of Mathematics: "))
marks4 = int(input("Enter Your marks of English: "))
marks5 = int(input("Enter Your marks of Urdu: "))

total_percentage = (100 *(marks1 + marks2 + marks3 + marks4 + marks5))/500

if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33 and marks4 >= 33 and marks5 >= 33):
    print("Congratulation, You are pass for all subjects and you got:", total_percentage,"% marks")

else:
    print("You Failed, try again next year and you got:", total_percentage,"% marks")


# Q NO. 5: Detect spam messages in mail, message and any social media

p1 = "Make a lot of money" or "make a lot of money"
p2 = "buy now" or "Buy Now" or "Buy now"
p3 = "subscribe this" or "Subscribe this" or "Subscribe This"
p4 = "click on" or "Click on" or "Click On"

message = input("Enter your message: ")

if((p1 in message) or (p2 in message) or (p3 in message)or (p4 in message)):
    print("This message is a spam")
else:
    print("This message is not a spam")



# Q No. 6: Write a program to find whether a given username contains less then 10 charaters
username = input("Enter username: ")

if(len(username) < 10):
    print("Your username is contain less than 10 characters")
else:
    print("Your username is contain more than or equal to 10 characters")


# Q No. 7:
marks = int(input("Enter your marks: "))

if(marks <= 100 and marks >= 90):
    grade = "Ex"

elif(marks >= 90 and marks >= 80):
    grade = "A"

elif(marks >= 80 and marks >= 70):
    grade = "B"

elif(marks >= 70 and marks >= 60):
    grade = "C"

elif(marks >= 60 and marks >= 50):
    grade = "D"

elif(marks < 50):
    grade = "F"

print("Your grade is:", grade)


# Detection ----->
post = input("Enter the post: ")

if("Akku" in post):
    print("this post is talking about Akku")

else:
    print("this post is not talking about Akku")






