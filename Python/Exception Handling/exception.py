# EXCEPTIOLNS: Exception are unexpected events or errors
# that occures durings the excetion of a program, which disrupts
# the normal flow of the program

Exception # keywords: try, except, else, finally

# a = int(input("Enter your number: "))
# print(10/a)
# print("OK I have DONE!")



# a = int(input("Enter your number: "))
# try:
#     print(10/a)
# except ZeroDivisionError:
#     print("sorry you cannt divide by 0\n")

# print("OK, I HAVE DONE THE DIVISION!")



# a = int(input("Enter your number: "))
# try:
#     print(10/a)
# except Exception as err:
#     print(f"sorry there is an err as {err}\n")
# else:
#     print("there is no exception")
# finally:
#     print("I will run always no matter what!")

# print("OK, I HAVE DONE THE DIVISION!")



age = int(input("Enter your age: "))

if age < 10 or age > 18:
    raise ValueError("Sorry! your must be between 10 and 18")
else:
    print("Welcome to the clup")

print("The clup will start soon")