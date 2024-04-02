import math

class Shape:
    def area(self):
        raise NotImplementedError

    @staticmethod
    def is_triangle_right(a, b, c):
        sides = sorted([a, b, c])
        return sides[0]**2 + sides[1]**2 == sides[2]**2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self):
        return self.is_triangle_right(self.a, self.b, self.c)