# Abstraction = Hiding the complex details and showing only the essential features.

# It means we show only what’s necessary to the user and hide the internal working (complex logic).

from abc import ABC, abstractmethod
class abstract(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    def area(self):
        pass


class Squar(abstract):
    def __init__(self, side):
        self.side = side


class Circle(abstract):
    def __init__(self, radius):
        self.radius = radius


    def perimeter(self):
        print("I have created")


    def area(self):
        print("I have created this")


obj = Circle(7)