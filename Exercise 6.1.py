class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def length(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __hash__(self):
        return hash((self.x, self.y, self.z))

# Exemplary tests.
import math
v = Vector(5, 7, -2)
w = Vector(4, -9, 1)
assert v != w
assert v + w == Vector(9, -2, -1)
assert v - w == Vector(1, 16, -3)
assert v * w == -45
assert v.cross(w) == Vector(-11, -13, -73)
assert v.length() == math.sqrt(78)
S = set([v, v, w])
assert len(S) == 2

print("Tests passed")