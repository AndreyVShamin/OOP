# Методы инициализации

class Cat:
    """
    OOP6
    """

    def __init__(self, name, breed='pers', age=1, color='white', test: bool = True):
        """
        oop6 __init__
        :param name: string
        :param breed: string
        :param age: int
        :param color: string
        :param test: bool
        """
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

