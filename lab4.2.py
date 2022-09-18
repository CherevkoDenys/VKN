import math
x, y=float(input("введіть текст 1")), float(input("введіть текст 2"))
U=(x*math.log10(y))+(1/(x**2+y**2+0.3))-math.e**(6*x-y)
print(U)