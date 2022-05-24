bit_utf = b'r\xc3\xa9sum\xc3\xa9'
print(bit_utf)
str_utf = bit_utf.decode("utf-8")
print(str_utf)
bit_latin = str_utf.encode("Latin1")
print(bit_latin)
str_latin = bit_latin.decode("Latin1")
print(str_latin)