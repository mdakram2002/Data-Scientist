# Polymorphism means — “one name, many forms.”
# In programming, it allows the same function or method to behave differently depending on the object or data type.


# In Python OOP, polymorphism lets you:
# Use the same method name in different classes.
# The behavior of that method depends on the object calling it.

class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):  # overrides parent method
        print("Bark Bark!")

class Cat(Animal):
    def sound(self):  # overrides parent method
        print("Meow Meow!")

# Create objects
a = Animal()
d = Dog()
c = Cat()

a.sound()  # Output: Some generic animal sound
d.sound()  # Output: Bark Bark!
c.sound()  # Output: Meow Meow!

