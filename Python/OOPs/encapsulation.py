# Encapsulation = Data Hiding + Controlled Access

# It means we bundle data (variables) and methods (functions) together inside a class,
# and we protect some data from being directly accessed or modified from outside.


class Person:
    def __init__(self, name, age):
        self.name = name               # public
        self._address = "Bihar"        # protected
        self.__salary = 30000          # private

    def show_info(self):
        print("Name: ", self.name)
        print("Age: ", self._address)
        print("Salary: ", self.__salary)



p1 = Person("Akram", 22)
p1.show_info()


# when we access outside of the class show_info
# print(p1.name)
# print(p1._address)
# print(p1._Person__salary)  # ✅ works but breaks encapsulation
# print(p1.__salary) #AttributeError: 'Person' object has no attribute '__salary'



class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    # gatter
    def get_age(self):
        return self.__age


    # setter
    def set_age(self, new_age):

        if new_age > 0:
            self.__age = new_age
        else:
            print("Invalid Age!")


p1 = Person("Akram", 22)
print(p1.get_age())

p1.set_age(24)
print(p1.get_age())

# print(p1.set_age(-5))