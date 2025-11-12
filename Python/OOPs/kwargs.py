
def information(**kwargs):
    print("your information: ")
    for i in kwargs:
        print(f"{i},", kwargs)

information(name = "Akram", age = 22, designation = "AI Engineer")


