import json

dict1 = {
    "111111": ("Viva", "5"),
    "222222": ("Missi", "15"),
    "333333": ("Lili", "35"),
    "444444": ("Roza", "55"),
    "555555": ("Lisa", "65"),
    "666666": ("Max", "95"),
}


with open("data.json", "w") as write_file:
    json.dump(dict1, write_file)
