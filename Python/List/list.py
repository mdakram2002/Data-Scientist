
# Mutable:- Mutability refers to whether an object's value can be changed after data creation. And list allows this.
# mutable means you can change variable after creation

# creation of list
# a = [1,2,3,4,5, "hell0", 33]


#1st way using index
# for i in range(len(a)):
#     print(a[i])

# for i in a:
#     print(i)
# help(list)


l = [1,25,6, 0, -1, -33, 33, -2]
# l[2] = 22
# print(l[2])


# PRINT POSTIVE AND NIGATIVE NUMBER IN LIST
# print("Postive Element are: ")
# for i in l:
#     if i > 0:
#         print(i)

# print("Nigative Elements are: ")
# for i in l:
#     if i < 0:
#         print(i)



# MEAN OF LIST ELEMENT
# l = [1,2,3,66,78,7,3,0]
# sum = 0

# for i in l:
#     sum = sum + i

# print(sum)
# print(f"Mean of List l: {sum/len(l)}")




# FIND THE GREATEST ELEMENT IN LIST
# l = [1,2,33,4,5,77,0]

# largest = l[0]
# idx = 0

# for i in range(len(l)):

#     if l[i] > largest:
#         largest = l[i]
#         idx = i
# print(f"Your Largest Number is: {largest} at index: {idx}")



# l = [1,22,33,4,77,35]
# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i

#     # Edge: for after largest read then print if exist (ex: 35) sec_largest
#     elif i > sec_largest:
#         sec_largest = i
# print(sec_largest, largest)



#CHECK LIST IS SORTED OR NOT?
a = [11,22,33,44,55]

for i in range(len(a) - 1):
    if a[i] < a[i+1]:
        continue
    else:
        print("your list is not sorted")
        break
else:
    print("your list is sorted")

