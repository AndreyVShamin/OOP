
class Car:
    model = "BMW"
    engine = 1.6

a1 = Car()
a2 = Car()
print(a1.__dict__)
a1.seat = 4
a1.model = "LADA"
print(a1.__dict__)

print(a2.__dict__)
print(Car.__dict__)
