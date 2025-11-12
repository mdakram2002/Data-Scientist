# Single Inheritance
class Parent:
    def show(self):
        print("This is the parent class")

class Child(Parent):
    def display(self):
        print("This is the child class")

obj = Child()
obj.show()
obj.display()



# Multiple Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal:", name)

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Human:", name, age)

class Robot(Animal, Human):
    name3 = "Nadiya@@"

    def __init__(self, name, age):
        Animal.__init__(self, name)
        Human.__init__(self, name, age)
        print("Robot Created")

obj = Robot("Alexa", 5)



# Multilevel Inheritance
class Factory:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips
        print("Factory initialized")

class BiharFactory(Factory):
    def __init__(self, material, zips, color):
        super().__init__(material, zips)
        self.color = color
        print("BiharFactory initialized")

class JaipurFactory(BiharFactory):
    def __init__(self, material, zips, color, pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets
        print("JaipurFactory initialized")

obj = JaipurFactory("Leather", 3, "Black", 2)




# Hierarchical Inheritance
class Vehicle:
    def fuel(self):
        print("Every vehicle needs fuel")

class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")

class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")

car = Car()
bike = Bike()

car.fuel()
bike.fuel()



# Hybrid Inheritance
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C:
    def showC(self):
        print("Class C")

class D(B, C):
    def showD(self):
        print("Class D")

obj = D()
obj.showA()
obj.showC()
