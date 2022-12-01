from array import*
import numpy as np
import random 
m,n,k,l = 4, 5 ,2 ,10
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

while a > b:
   print("a має бути менше b")
   a = int(input("Введіть перше число: "))
   b = int(input("Введіть друге число: "))

A = np.zeros((m,n))
for i in range(m):  
    for j in range (n):     
          A[i][j] = random.randint(a,b) 
          
B = A.copy()
B.shape = (k,l) 
C =  sum(map(np.array, B))
print("Array A:\n", A, "\nArray B:\n", B, "\nArray C:\n", C) 



