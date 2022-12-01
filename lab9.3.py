addresses = {}
descriptions = {}

for i in range(5):
    address = input("Enter site address")
    description = input("Enter side description")
    addresses[i] = address
    descriptions[i] = description

for i in range(5):
    print(f'{addresses[i]} - {descriptions[i]}')