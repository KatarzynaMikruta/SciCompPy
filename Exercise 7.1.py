class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def find_axis(v1, v2):
        if v1.cross(v2) == Vector(0, 0, 0):
            raise ValueError("Vectors are parallel or zero")
        else:
            return v1.cross(v2)

# cross test
import math
v = Vector(5, 7, -2)
w = Vector(4, -9, 1)
assert v.cross(w) == Vector(-11, -13, -73)
print("Cross test passed")

# function test
a = Vector(0, 0, 0)
b = Vector(1, 2, 3)
c = Vector(2, 4, 6)
d = Vector(4, 5, 6)
#print(a.find_axis(b))  # with zero vector
#print(b.find_axis(c))  # parallel vectors
print(c.find_axis(d))