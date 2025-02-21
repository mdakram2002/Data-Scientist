# What is Sets in Python?
'''A set is a collection of unique and unordered elements. Sets are useful when you need to store multiple items,
but you only want each item to appear once. They are defined by enclosing elements in curly braces {} or using
the set() function.'''

# Key Features
# Unordered:
'''The elements in a set do not have a defined order.'''
# Immutable Elements:
'''Elements of a set must be immutable (e.g., numbers, strings, tuples), but the set itself is mutable.'''
# No Duplicates:
'''Sets automatically handle duplicates by storing only one occurrence of each element.'''
# UnIndex:
''' Sets are unindexed, that means cannot element by index'''



s = {1,2,3,44,5,"Akku", True}
# print(s)

s.add("Raj")
# print(s)

s1 = {1,2,3,44,5}
print("SET S1: ",s1)

s2 = {31,32,3,64,5}
print("SET S2: ",s2)


#----------------------------------------------------( SET METHODS )------------------------------------------------------------#
# union of set methods
print("UNION: ", s1.union(s2))

# intersection of set method
print("INTERSECTION: ",s1.intersection(s2))

# Using isSupper set method
print("isSupper: ",s1.isSupperset({1, 3}))


# Using pop method
print(s1.pop())

s1.clear()
# print("Clear S1: ",s1)

words = {
    "man":"Aadmi",
    "woman":"aurat",
    "apple": "seb",
    "cat": "billi"
}
word = input("Enter the word you want meaning of: ")
print(words[word])

s = set()

n = input("Enter the number you want to print: ")
s.add(int(n))
n = input("Enter the number you want to print: ")
s.add(int(n))
n = input("Enter the number you want to print: ")
s.add(int(n))
n = input("Enter the number you want to print: ")
s.add(int(n))
n = input("Enter the number you want to print: ")
s.add(int(n))
n = input("Enter the number you want to print: ")
s.add(int(n))
n = input("Enter the number you want to print: ")
s.add(int(n))
n = input("Enter the number you want to print: ")
s.add(int(n))
n = input("Enter the number you want to print: ")
s.add(int(n))
print("HERE IS THE SET: ", s)


s = set()
s.add(20)
s.add(20.0)
s.add("20") # length of a after these operations

print("HERE IS THE SET: ", s)

dic = {}
print("HERE IS", dic)
print(type(dic)) # <class 'dict'>

name = input("Enter the name of you're friend name:")
lang = input("Enter the language name:")
dic.update({name: lang})

name = input("Enter the name of you're friend name:")
lang = input("Enter the language name:")
dic.update({name: lang})

name = input("Enter the name of you're friend name:")
lang = input("Enter the language name:")
dic.update({name: lang})

name = input("Enter the name of you're friend name:")
lang = input("Enter the language name:")
dic.update({name: lang})

name = input("Enter the name of you're friend name:")
lang = input("Enter the language name:")
dic.update({name: lang})

name = input("Enter the name of you're friend name:")
lang = input("Enter the language name:")
dic.update({name: lang})
print("HERE IS THE DICT: ",dic)



s = {2, 4, 5, 6, [2, 4,], "Akku"}
print("HERE IS THE DICT: ",s)

