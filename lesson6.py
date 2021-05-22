# Методы инициализации

class Cat:

    def __init__(self, name, breed='pers', age=1, color='white', test: bool = True):
        print('hello new object is ', self, name, breed, age, color)
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
        self.test = test


bob = Cat("Robert")
kitty = Cat(age=14, name="Tasya", breed="Unknown", color=("Red", "Black", "White"))

print(bob.__dir__())
bob.bool = "False"

