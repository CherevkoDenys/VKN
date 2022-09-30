import math
A=float(input("введіть перше число:    "))
B=float(input("введіть друге число:    "))
C=float(input("введіть третє число:    "))
O=0.0
if B>A and C>A:
   print('А-найменше')
elif B>C and A>C:
   print('С-найменше')
if C>B and A>B: 
   print('В-найменше')