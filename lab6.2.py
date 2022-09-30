import math
a=float(input("введіть діапазон (а):     "))
b=float(input("введіть діапазон (b):     "))
h=float(input("введіть крок (h)     "))
x=a
while x<b:
   y=(x**3+1*math.fabs(x))/3**x
   print("x=%.1f   y=%.3f"%(x,y))
   x=x+h