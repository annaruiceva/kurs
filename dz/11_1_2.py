def geoGen(start, q, stop):
    while True:
        if stop <= 0:
            return
        yield start
        start *= q
        stop -= 1


generator3 = geoGen(2, 2, 5)
for i in generator3:
    print(i, end=" ")
