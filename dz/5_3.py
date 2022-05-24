start_tuple = ("apple", "maam", "hey", "daeead", "dodo")
new_tuple = tuple(
    filter(lambda t: t == t[::-1], start_tuple)
)
print(new_tuple)
