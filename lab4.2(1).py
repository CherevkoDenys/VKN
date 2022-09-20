import math
def func1(x1,x2):
    U=((x1)*math.log10((x2)))+(1/((x1)**2+(x2)**2+0.3))-math.e**(6*(x1)-(x2))
    return(U)
x, y=float(input("введіть текст :")), float(input("введіть текст :"))
U=func1(x,y)
print(U)