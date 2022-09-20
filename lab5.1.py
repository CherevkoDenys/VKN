import math
x=float(input("введіть число х:      "))
def f1(x1):
   rez=7*math.log1p(x1)+math.log(x1,7)+math.log10(x1)
   return(rez)
def f2(x2):
   rez=math.sin(x2)-math.cos(x2+2+math.pi/7)
   return(rez)
def f3(x3):
   rez=2.24*math.e**(0.5*x3+0.1)*2**(0.3*x3)
   return(rez)
y=0.0
if x >= 1.0:
    y=f1(x)
elif -10.3 < x < 1.0:
    y=f2(x)
elif x <= -10.3:
    y=f3(x)
print(y)