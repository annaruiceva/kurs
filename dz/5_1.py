func = lambda num: "четное" if num % 2 == 0 else "нечетное"
try:
    print(func(int(input("Введите число: "))))
except ValueError:
    print("Введите целое число!")
