


class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Hello how are you: {self.name}"


obj = Animal("Cat")
print(obj)
