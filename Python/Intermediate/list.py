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
# print(list1)

# reverse method in Python:
# reverse the data of list's list1.
list1.reverse()
print(list1)

# insert method in Python:
# insert at the index[4] of list's list1.
list1.insert(4, "Aman")
print(list1)

# pop/remove method in Python:
# delete/remove at the index[4] of list's list1.
list1.pop(3)
print(list1)