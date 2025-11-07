# DISCTIONARY


# d = {1:"Hello", 2:"Akram"}

# print(d)
# print(type(d))

d = {1:10, 2:20, 3:30, 4:40, 5:50}

# d[1] = 100 #updating the value of 1
# d[6] = 60 #creating the new key-value pair
# del d[4] #deleting the key-val of 4
# print(d)

for i in d:
    print(i) #key
    print(d[i]) #val

# directly access val
# for i in d.values():
#     print(i)


# MARGE TOW DISCTIONARY IN ONE
# d1 = {1:10, 2:20, 3:30, 4:40, 5:50}
# d2 = {6:60, 7:70, 8:80, 9:90, 10:100}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)


# OCCURENCE OF NUMBER
# l = [1,2,2,2,2,3,4,4,4,5,6,7,7,7,8,8,8]

# d = {}
# for i in l:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)



d1 = {1:10, 2:20, 3:30, 4:40, 5:50}
d2 = {5:50 ,6:60, 7:70, 8:80, 9:90, 10:100}

for i in d2:
    if i in d1.key():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]

