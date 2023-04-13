class shape:
    def area(self):
        return 0


class TRIANGLE(shape):
    def __init__(self, base, height):
        self.mybase = base
        self.myheight = height

    def area(self):
        print(0.5 * self.mybase * self.myheight)


class RECTANGLE(shape):
    def __init__(self, length, width):
        self.mylength = length
        self.mywidth = width

    def area(self):
        print(self.mywidth * self.mylength)


measurement2 = TRIANGLE(12, 6)
measurement2.area()
measurement1 = RECTANGLE(12, 15)
measurement1.area()
