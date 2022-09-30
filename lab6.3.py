import math
a=float(input("введіть діапазон (а):     "))
b=float(input("введіть діапазон (b):     "))
h=float(input("введіть крок (h)     "))
spisok=[]
x=a
while x<b:
   y=(x**3+1*math.fabs(x))/3**x
   spisok.append(y)
   x=x+h
print(spisok)