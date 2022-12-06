rucksacks_list = []
priority_list = []
priority_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, \
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,\
        'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, \
            'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, \
                'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

with open('input.txt', 'r') as f:

    data = f.readlines()

    for line in data:
        string_length = len(line)
        half_string_length = int(string_length / 2)
        first_half_string = line[:half_string_length]
        second_half_string = line[half_string_length:]
        line = [first_half_string, second_half_string.strip('\n')]
        rucksacks_list.append(line)

print(rucksacks_list)

for item in rucksacks_list:
    character_already_counted = False
    for character in item[0]:
        if character in item[1] and not character_already_counted:
            priority_list.append(priority_dict[character])
            character_already_counted = True

print(priority_list)
print(sum(priority_list))