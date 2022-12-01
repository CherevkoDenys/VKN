import math 
import json
students = {'Васильченко Діана': 3, 'Ляшенко Крістіна': 2, 'Полюхович Анна': 5, 'Рибачок Ірина': 4, 'Скороход Віталій': 5, 'Черевко Денис': 3, 'Білоусова Вероніка': 4,
            'Іванов Кирил': 3, 'Гальчинська Софія': 5}
with open("D:\Git\Repos\VKN\students 1-8.txt",  'w', encoding='utf-8') as outfile:
    json.dump(students, outfile)
sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)
scholarship_size = math.floor(students.__len__()*0.4)
print('Students whose can get scholarship: ')
for i in range(0, scholarship_size):
    print(sorted_students[i])
    
