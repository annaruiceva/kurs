def num(number):
    try:
        print("отрицательное" if number < 0 else "ноль" if number == 0 else "положительное")
    except:
        print("введите число!!!")


num(float(input("введите число: ")))
