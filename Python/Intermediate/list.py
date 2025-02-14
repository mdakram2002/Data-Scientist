# What is a List?
'''A list is a mutable, ordered collection of elements in Python. Lists can store elements of
various data types, including integers, strings, and even other lists. They are one of the most
commonly used data structures due to their flexibility and ease of use.'''

# Creating a List
'''You can create a list by placing a comma-separated sequence of elements within square brackets []:'''

# List in Python:-
# list is a type of constainer to store a any data type
# for Example:

friends = ["Akram", "Ajju,", "Faisu", "Sajid",886, False, True]
# print(friends[6]) # True
# print(friends[0]) # True

friends[0] = "Aman" #Unlike Strings lists are mutable
# print(friends[0])
# print(friends[0:7]) # Access all the data from list's friends,


#-------------------------------------------------------------------------------------------------#
#------------------------------------Methods of List in Python------------------------------------#


# index start from 0 in this implementation.
print()
friends = ["Akram", "Ajju,", "Faisu", "Sajid",886, False, True]
# print(friends)

# Append method in Python:
# insert/add at the end of list's friends.
friends.append("Aman")
# print(friends)

# sort method in Python:
# accending/increasing order of list data.
list1 = [11, 33, 22, 44, 55]
list1.sort()
print("Sort method: ", list1)

# reverse method in Python:
# reverse the data of list's list1.
list1.reverse()
print("Reverse method: ", list1)

# insert method in Python:
# insert at the index[4] of list's list1.
list1.insert(4, "Aman")
print("Insert method: ", list1)

# pop/remove method in Python:
# delete/remove at the index[4] of list's list1.
list1.pop(3)
print("Pop method: ", list1)