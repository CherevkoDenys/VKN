import math
x=float(input())
y=(math.sin(2*x)/math.cos(2*x))+(math.cos(4*x-x**0.5))-(2/(abs(x-1)+0.1)**(1./3.))
print(y)