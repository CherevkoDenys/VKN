sites = ('https://www.youtube.com/', 'https://github.com/', 'https://leetcode.com/', 'https://www.google.com/')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
chars = {}
for site in sites:
    for char in site:
        if char in alphabet:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

max_value = 0
for char in chars:
    if chars[char] > max_value:
        max_value = chars[char]
for char in chars:
    if chars[char] == max_value:
        print(f'{char}: {max_value}')