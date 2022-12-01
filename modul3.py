import math
def V(a,b,c):
    S1 = (math.pow(a,2)*math.sqrt(3))/4
    S2 = (math.pow(b,2)*math.sqrt(3))/4
    d = (c/3)*(S1+math.pow((S1*S2),2)+S2)
    print("V=",d)
f = float(input("Введіть сторону нижньої основи: "))
g= float(input("Введіть сторону верхньої основи: "))
h = float(input("Введіть висоту піраміди: "))
V(f,g,h)

def S(a,b,c):
    S=S1+S2+S3
    S1 =((3*a)/2+(3*b)/2)/c
    S2 = (math.pow(a,2)*math.sqrt(3))/4
    S3 = (math.pow(b,2)*math.sqrt(3))/4
    print("S=",S)
k = float(input("Введіть сторону нижньої основи: "))
l= float(input("Введіть сторону верхньої основи: "))
h = float(input("Введіть висоту піраміди: "))
S(k,l,h)




    
    