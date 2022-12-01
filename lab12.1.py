input = 'C:\\Users\\Sasha\\.vscode\\vkn\\lab12\\input.txt'
output = 'C:\\Users\\Sasha\\.vscode\\vkn\\lab12\\output.txt'

def read_from_file(input):
    with open(input, "r") as data:
        my_list = []
        for line in data:
            items = line.split(":")
            my_list.append({items[0]: int(items[1])})
        return my_list


def write_keys(data, input):
    with open(input, "w") as file:
        for el in data:
            for key in el.keys():
                file.write(key)
                file.write("\n")


def print_unique_value(data):
    vals = []
    for el in data:
        for value in el.values():
            vals.append(value)

    for value in set(vals):
        print(value)


my_list = read_from_file(input)
for el in my_list:
    print(el)

write_keys(my_list, output)
print_unique_value(my_list)