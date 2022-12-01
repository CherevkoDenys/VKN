import random
import modull2

numbers=[]
for j in range(random.randint(1,9)):
    numbers.append(modull2.generate())
print(numbers)

unique_numbers =[]
for g in numbers:
     for value in g.values:
        if g not in unique_numbers:
           unique_numbers.append(value)
     for value in set(unique_numbers):
        print(len(value))