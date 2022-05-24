from random import randint

int_list = [randint(0, 10) for x in range(randint(0, 10))]
str_list = list(map(lambda x: str(x), int_list))
print(int_list, str_list, sep="\n")
