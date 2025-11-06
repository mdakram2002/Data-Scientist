# DEEP COPY

# a = [1,2,3,4,5]
# #Values of a is deeply copy in b
# b = a
# b[0] = 100
# print(a)

# SHALLOW COPY

a = [1,2,3,4,5]

b = a.copy()
b[0] = 100

print(a)

help(dict)
