# What is a Tuple?
'''A tuple is a collection data type in Python that is ordered and immutable.This means once a tuple
is created, its values cannot be changed. Tuples are usedto group together related data and are
defined by placing elements within parentheses () separated by commas.'''


a = ( 2, 4, 5, 1)
# print(type(a))  #<class 'tuple'>

b = (1, "Akram", False, True, 33, "Amaan")
# print(b)
# print(b[0])
# print(b[1])
# print(b[2])
# print(b[3])
# print(b[4])
# print(b[5])
# print(type(b)) # Do not change tuple elements.

# count = a.count(1)
# print(count)

i = a.index(1)
print(i)


# Packing and Unpacking Tuple in Python--->
# packing tuple in Python:
tple = 1, 2, 3
# print(tple)


# unpacking tuple in Python
a, b, c = tple
# print(a, b, c)



# Immutability------>
''' Tuples are immutable, meaning their elements cannot be changed once assigned. '''
tple[0] = 10 # TypeError: 'tuple' object does not support item assignment
print(tple)


## Use Cases of Tuples
# Returning multiple values from a function:
'''Functions can return multiple values in the form of a tuple.'''

# Storing heterogeneous data:
'''Tuples can store multiple data types, making them suitable for grouping diverse data.'''

# Dictionary keys:
'''Tuples can be used as keys in dictionaries because they are immutable.'''

# Function returning multiple values