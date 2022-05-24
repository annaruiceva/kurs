try:
    print("отрицательное" if (number := float(input("введите число: "))) < 0 else "ноль" if number == 0 else "положительное")
except:
    print("введите число!!!")
