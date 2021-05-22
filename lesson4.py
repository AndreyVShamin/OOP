########################

class Car:
    model = "BMW"
    engine = 1.6

    @staticmethod
    def drive():
        print("Let's go")


print(Car.__dict__)
Car.drive()
getattr(Car, "drive")()

a = Car()
a.drive()

