
class Cat:
    breed = 'pers'
    def hello(*args):
        print("Hello world from kitty", args)

    def set_value(self, value, age=0):
        self.name =value
        self.age = age

    def show_breed(instance):
        print(f"my breed is {instance.breed}.")

    def show_name(instance):
        if hasattr(instance, 'name'):
            print(f"my name is {instance.name}")
        else:
            print("noname")


    def set_value(koshka, value, age=0):
        koshka.name  = value
        koshka.age = age

Cat.hello()
a = Cat()
a.hello()
print(a)
a.show_breed()
a.breed = "siam"
print(a.__dict__)

mary = Cat()
mary.show_name()
mary.name = "Mary"
mary.show_name()

tom = Cat()
tom.show_name()
tom.set_value("Tom")
tom.show_name()
print(tom.age)


