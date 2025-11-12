# class: A class is a user-defined data type where all the members functions and data members are defined based on specific requirments. These members can be accessed using an object.
# or A class is a blueprint that defines functions which are used by an object

# class Factory:
#     a = 12
#     def hello(self):
#         print("how are you")
#     # print("Hello, how are you i am getting initialized: ")
# obj = Factory()

# print(obj.a)
# obj.hello()



# class Animal:
#     def __init__(self, cat, dog, elef):
#         self.cat = cat
#         self.dog = dog
#         self.elef = elef

#     def show(self):
#         print(f"Your Animals are {self.cat}, {self.dog}, {self.elef}")

# eat = Animal("Eat", 1,2)
# eat1 = Animal("Eat", 1,2)



class Person:
    def __init__(self, age):
        self.age = age   # 'self' refers to the current instance

p1 = Person(25)
print(p1.age)  # Output: 25
# Here,

# self.age means “set the age attribute of this object to the passed value.”

# It’s like writing this.age = age in Java or C++.
# ✅ self refers to the current object instance, just like this in other object-oriented



# class Factory:
#     a = "I am an attribute mentioned inside factory"
#     def hello(slef):
#         print("Hello I am a method mentioned inside factory")

# class FactoryPune(Factory):
#     pass



# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"Hello, your name is {self.name} and age is {self.age}")

# class Human(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

# animal = Animal("Cat")
# person1 = Human("akkk", 22)

# person1.show()
# animal.show()

