import math

class Cylinder:
    # Constructor to store radius and height
    def __init__(self, r, h):
        self.r = r
        self.h = h

    #Curved Surface Area of Cylinder
    def csa(self):
        return 2 * math.pi * self.r * self.h
    
    # Total Surface Area of Cylinder
    def tsa(self):
        return 2 * math.pi * self.r * (self.r + self.h)
    # Volume of Cylinder
    def volume(self):
        return math.pi * self.r * self.r * self.h


class Cone:
    # Constructor stores radius and height
    def __init__(self, r, h):
        self.r = r
        self.h = h
        # Slant height
        self.l = math.sqrt(r*r + h*h)  
    
    # Curved Surface Area of Cone
    def csa(self):
        return math.pi * self.r * self.l
    
    # Total Surface Area of Cone
    def tsa(self):
        return math.pi * self.r * (self.r + self.l)
    
    # Volume of cone
    def volume(self):
        return (1/3) * math.pi * self.r * self.r * self.h


class Cube:
    def __init__(self, a):
        self.a = a
    
    # CSA of Cube
    def csa(self):
        return 4 * self.a * self.a
    
    # TSA of Cube
    def tsa(self):
        return 6 * self.a * self.a
    
    # Volume of Cube
    def volume(self):
        return self.a ** 3


class Cuboid:
    # Constructor stores length, breadth & height
    def __init__(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h
    
    # CSA of Cuboid
    def csa(self):
        return 2 * self.h * (self.l + self.b)
    
    # TSA of Cuboid
    def tsa(self):
        return 2 * (self.l*self.b + self.b*self.h + self.h*self.l)
    
    # Volume of Cuboid
    def volume(self):
        return self.l * self.b * self.h


# Constructor stores radius
class Sphere:
    def __init__(self, r):
        self.r = r

    # CSA of Sphere
    def csa(self):
        return 4 * math.pi * self.r * self.r
    # TSA of Sphere
    def tsa(self):
        return 4 * math.pi * self.r * self.r
    # Volume of Sphere
    def volume(self):
        return (4/3) * math.pi * self.r**3
