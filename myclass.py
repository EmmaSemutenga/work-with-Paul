# class MyClass:
#     i = 12345

#     def __init__(self, name):
#         self.name = name

#     def f(self):
#         return "Hello World"

# x = MyClass("Paul")

# print(x.f())
# class Person:
#     species = "Human"

# john = Person()
# print(john.species)
# Person.alive = True
# john.alive = False
# print(john.alive)
# tom = Person()
# print(tom.species, tom.alive)
# # print()
# john.age = 27
# print(john.age)
# print(Person.age)

class Toyota:
    produced_cars = 0

    def __init__(self, tires=None, color="purple"):
        Toyota.produced_cars += 1
        self.tires = tires
        self.color = color

    def move(self):
        return f"{self.tires}--{self.color}"

        

corona = Toyota(3, "red")

# Toyota.produced_cars = Toyota.produced_cars + 1
vitz = Toyota(4, "yellow")

# Toyota.produced_cars = Toyota.produced_cars + 1

print(vitz.color)
print(vitz.produced_cars)
# print(vitz.car_detail())
