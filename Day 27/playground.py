def add(*args):
    list = []
    for n in args:
        list.append(n)
    print(sum(list))

add(1, 3, 5, 7)

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]

calculate(3, add=3, multiply=3)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make= "Nissan", model="GT-R")
print(my_car.model)
