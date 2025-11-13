import math

class Cylinder:
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def csa(self):
        return 2 * math.pi * self.r * self.h

    def tsa(self):
        return 2 * math.pi * self.r * (self.r + self.h)

    def volume(self):
        return math.pi * self.r * self.r * self.h


class Cone:
    def __init__(self, r, h):
        self.r = r
        self.h = h
        self.l = math.sqrt(r*r + h*h)  # slant height

    def csa(self):
        return math.pi * self.r * self.l

    def tsa(self):
        return math.pi * self.r * (self.r + self.l)

    def volume(self):
        return (1/3) * math.pi * self.r * self.r * self.h


class Cube:
    def __init__(self, a):
        self.a = a

    def csa(self):
        return 4 * self.a * self.a

    def tsa(self):
        return 6 * self.a * self.a

    def volume(self):
        return self.a ** 3


class Cuboid:
    def __init__(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h

    def csa(self):
        return 2 * self.h * (self.l + self.b)

    def tsa(self):
        return 2 * (self.l*self.b + self.b*self.h + self.h*self.l)

    def volume(self):
        return self.l * self.b * self.h


class Sphere:
    def __init__(self, r):
        self.r = r

    def csa(self):
        return 4 * math.pi * self.r * self.r

    def tsa(self):
        return 4 * math.pi * self.r * self.r

    def volume(self):
        return (4/3) * math.pi * self.r**3
