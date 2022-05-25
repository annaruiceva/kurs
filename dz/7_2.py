from time import sleep
from Auto import Auto


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color="Default", weight=0):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("Attention")
        print("move")

    def load(self):
        sleep(1)
        print("load")
        sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color="Default", weight=0):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        print("move")
        print(f"max speed is {self.max_speed}")


truck1 = Truck("Merida", 7, "sedan", 35)
car1 = Car("BmV", 12, "kupe", 365)

truck1.move()
print("-" * 10)
truck1.load()
truck1.birthday()
truck1.stop()
print("-" * 10)
truck1.info()
print("-" * 10)

car1.birthday()
car1.info()
print("-" * 10)
car1.move()
car1.stop()
