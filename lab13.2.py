from random import randint
from vector import Vector
vector = Vector

v1 = Vector("vector1", randint(-20, 20), randint(-20, 20), randint(-20, 20), randint(-20, 20))
v2 = Vector("vector2", randint(-20, 20), randint(-20, 20), randint(-20, 20), randint(-20, 20))
vectors = [v1, v2]

print(v1.plus(v2))

for vector in vectors:
    if vector.x1 < 0 and vector.y1 < 0 and vector.x2 < 0 and vector.y2 < 0:
        vector.showName()