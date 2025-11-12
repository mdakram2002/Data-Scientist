
# What is a Decorator?
'''
A decorator in Python is a special function that:
Modifies the behavior of another function — without changing its actual code.

In simple terms:
You “wrap” a function inside another function.
The wrapper can add extra functionality (like logging, validation, printing,
timing, etc.) before or after the original function runs.
'''


def decorator(func):
    def wrapper(a, b):
        print("I will print myself befor the funciton hello()")
        func(a, b)
        print("Now, Again after the function")
    return wrapper

@decorator
def hello(a, b):
    print("Hello I am in decorator: ")

hello()