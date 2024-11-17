name = "Akram"


# nameShort = name[index_start:index_end] #start form index 0 all the way till index_end
nameShort = name[0:6]
print(nameShort)



# Negative slicing in Python
nameOfAkram = "Akram"
# print(nameOfAkram[-6:0])
# print(nameOfAkram[0:6])

# print(nameOfAkram[0:])
# print(nameOfAkram[0:6])

# both the above line are true
# print(nameOfAkram[:6])
# print(nameOfAkram[0:6])

print(nameOfAkram[1:4]) # from 0 digit to 4 digit are removed ans=kra
print(nameOfAkram[1:4:6]) # after k 2 digits are removed and=k