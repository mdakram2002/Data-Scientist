name = "Akram"

nameShort = name[0:5] # start from 0 index and end from 5 index
# print(nameShort)

character1 = name[1]
# print(character1)


# negative slicing in strings ------------------------------------------------------------------------------------->>>>
# print(name[:5]) # is same as print(name[0:5])
# print(name[0:]) # is same as print(name[0:5])

# print(name[1 : 4])
# print(name[-4 : -1])



# String functions ------------------------------------------------------------------------------------------------->>>>>

print(len(name)) # length of string
print(name.endswith("kram")) # end of string
print(name.endswith("raM")) # end of string

print(name.capitalize()) # capitalize the starting character