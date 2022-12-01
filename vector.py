import math

class Vector:
    def __init__(self, name, x1, y1, x2, y2):
        self.name = name
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def getLen(self):
        return math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)

    def plus(self, other):
        return math.sqrt((other.x2 - self.x1) ** 2 + (other.y2 - self.y1) ** 2)

    def showName(self):
        name = str(input("Введіть назву вектора: "))
        self.name = name
        print(self.name)

    def setCoords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2