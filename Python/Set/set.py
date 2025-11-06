a = { 1,2,3,4,5,6}
b = {2,3,4,5,9,7}


union_set = a.union(b)
intersection_set = a.intersection(b)

s = a|b # union
c = a&b # intersection
d = a-b

print(s)
print(c)
print(d)

# print(union_set) # fetch all data accept common
print(intersection_set) # common between a and b




