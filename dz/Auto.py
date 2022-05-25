class Auto:
    def __init__(self, brand, age, mark, color="Default", weight=0):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("move")

    def birthday(self):
        self.age += 1

    def stop(self):
        print("stop")

    def info(self):
        print(f"Brand = {self.brand}\nAge = {self.age}\nMark = {self.mark}")



