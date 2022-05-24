a = input("Введите 1 строку ")+"\n"
b = input("Введите 2 строку ")+"\n"
c = input("Введите 3 строку ")+"\n"
d = input("Введите 4 строку ")
file = open("text.txt", "w")
file.write(a+b)
file.close()
file = open("text.txt", "a")
file.write(c+d)
file.close()

