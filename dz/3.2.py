def out_function(string):
    string_set = set(i for i in string if i.isalpha())
    string_list = [(string.count(i)) for i in string_set]
    max_len = len(str(max(string_list)))
    for i in string_set:
        print(f"| {i} | {string.count(i):<{max_len}} |")


out_function(input('введите строку: '))
