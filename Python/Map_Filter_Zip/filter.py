
# def even(x):
#     if x%2 == 0:
#         return True
#     else:
#         return False

# a = [1,2,3,4,5,6,7,8,9]
# ans = filter(even, a)

# print(ans), #it will return object
# print(list(ans)) # now it will return list

a = [1,2,3,4,5,6,7,8,9]
ans = filter(lambda x: True if x%2 == 0 else False, a)
print(list(ans))



