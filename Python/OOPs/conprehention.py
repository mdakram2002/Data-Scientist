
# first take a variable and then apply loon on variable like i then range function
# List Comprehension
lst = [i for i in range(1, 21) if i % 2 != 0]   # i%2 != 0 → odd numbers
print("List Comprehension:", lst)


# Dictionary Comprehension
dct = {i: i**2 for i in range(1, 10)}
print("Dictionary Comprehension:", dct)



# Set Comprehension
st = {i for i in range(1, 31) if i % 3 == 0}
print("Set Comprehension:", st)
