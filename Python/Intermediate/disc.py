# What is Dictionary?
'''A dictionary in Python is a collection of key-value pairs, where each key is unique. Dictionaries are mutable,
meaning you can add, remove, or change elements after the dictionary is created.
They are defined using curly braces {} or the dict() constructor.'''

# Key Features of Python Dictionaries
# Unordered (as of Python 3.7): The order of elements is not guaranteed in versions before Python 3.7.
# Mutable: You can modify the dictionary after its creation.
# Unique Keys: Each key must be unique.


marks = {
    "Akku": 100,
    "Rohan": 100,
    "Gill": 100,
    "Martin": 100,
}
marks = [["akku",100], ["Rohan", "Gill"]]
print(type(marks)) # <class 'dict'>
print(marks[0])


employees = [{
    "Name": "Akram Shaikh",
    "Age": 21,
    "Id": 100,
    "Company": "Amazon",
    "Salary": "$1200",
},
{
   "Name": "Sajid Khan",
    "Age": 23,
    "Id": 101,
    "Company": "HP",
    "Salary": "$1200",
},
{
    "Name": "Majid Ali",
    "Age": 32,
    "Id": 103,
    "Company": "Uber",
    "Salary": "$1300",
},
{
   "Name": "Rashid Khan",
    "Age": 25,
    "Id": 104,
    "Company": "Google",
    "Salary": "$1400",
},
{
    "Name": "Wahid Ali",
    "Age": 45,
    "Id": 105,
    "Company": "Wiprow",
    "Salary": "$1400",
}]
print(employees)
print(employees[0])

# <------------------------------------------------------Methods in Dictionary------------------------------------------>


marks = {
    "Akku": 101,
    "Rohan": 102,
    "Gill": 103,
    "Martin": 104,
}
print(marks.items())   # items of the dictionary (keys and values)
print(marks.keys())    # keys of the dictionary
print(marks.values())  # values of the dictionary

marks.update({"Akku": 99})
# print(marks.items())

# Also add new key value pairs of existing dictionary becouse of it is mutable
marks.update({"Rani": 102})
print(marks.items())


print(marks.get("Raj"))
print(marks.get("Akku2"))   # Print NONE
# print(marks("Akku2"))     # Returns an error message

s = {1,2,3,4,5 ,6,7,8,9}
print(type(s))

e = set() # Don't use s = {} as it will be an empty dictionary
print("let's check what is this? ",e)
