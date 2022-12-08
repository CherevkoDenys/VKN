words=list(input('Введіть рядок ').split())
max=0
for i in words:
    if i.count("a")>max:
        max_a=i
        max=i.count("a")
print(max_a)