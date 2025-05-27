import math


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y  # y is up
        self.z = z

    def normalized(self):
        length = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        if length == 0:
            return Vector3(0, 0, 0)
        return Vector3(self.x / length, self.y / length, self.z / length)

    def cross(self, other: "Vector3"):
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def distance(self, other):
        x2 = (self.x - other.x) * (self.x - other.x)
        y2 = (self.y - other.y) * (self.y - other.y)
        z2 = (self.z - other.z) * (self.z - other.z)
        return math.sqrt(x2 + y2 + z2)


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def distance(self, other):
        x2 = (self.x - other.x) * (self.x - other.x)
        y2 = (self.y - other.y) * (self.y - other.y)
        return math.sqrt(x2 + y2)
