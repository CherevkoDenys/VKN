import math
x, y=float(input()) ,float(input())
U=(x*math.log(y))+(1/(x**2+y**2+0.3))-math.e**(6*x-y)
print(U)