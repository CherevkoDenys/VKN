n=int(input('введіть кількість слів ').strip())
words=[]
max=0
for i in range(n):
    words.append(input(f'Слово №{i} '))
    if max<len(words[i]):
        max=len(words[i])
for i in words:
    if len(i) != max:
        while len(i) != max:
            i="&"+i
    print(i)