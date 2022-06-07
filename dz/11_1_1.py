class GeoGenerator:
    def __init__(self, start, q, stop):
        self.start = start
        self.q = q
        self.stop = stop

    def __next__(self):
        res = self.start
        self.stop -= 1
        self.start *= self.q
        if self.stop < 0:
            raise StopIteration
        else:
            return res

    def __iter__(self):
        return self


gen = GeoGenerator(2, 2, 5)
for i in gen:
    print(i, end=" ")
