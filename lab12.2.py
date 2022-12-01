#2. Серійний номер двигуна складається з 7 випадкових цифр від 0 до 9, дефісу і року випуску (випадкове число
# у діапазоні [2000;2022]). Написати програму, яка запише у текстовий файл N випадкових номерів двигунів і 
#підрахує кількість унікальних номерів. Для генерування номера двигуна розробити функцію. 

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