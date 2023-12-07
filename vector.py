class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v2):
        return Vector(self.x + v2.x, self.y + v2.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __sub__(self, v2):
        return Vector(self.x - v2.x, self.y - v2.y)

    def __eq__(self, v2):
        self.x = v2.x
        self.y = v2.y
