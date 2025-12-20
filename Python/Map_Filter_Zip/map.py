# Map is used for applying a fucntion to multiple items.
# takes a list or any sequence
# Applies the same fuction to every item in that list


st = {1,2,3,4}
ans = map(lambda x : x*1, st)
print(set(ans))

# output : {8, 2, 4, 6}, (Set order changes because sets are unordered.)