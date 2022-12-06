import re

with open('pd_input.txt', 'r') as f:

    data = f.read()
    data = data.split("\n\n")
    stacks = data[0].split("\n")[:-1]
    print(stacks)

    number_of_columns = int(((len(stacks[0]) - 3) / 4) + 1)
    total_chars = len(stacks[2])
    print(total_chars)
    print(number_of_columns)

    new_stacks = {}
    # Let's try to parse the input so that we can get a list of dictionaries
    # Each dictionary will have a the key which represents the column for the stack
    for item in stacks:
        count = 0
        for char in item:
            count += 1
            # Let's get the first letter that shows up. It's always the 2nd character in the string.
            if count == 2:
                if '1' in new_stacks: # If the dictionary with key = '1' exists then...
                    new_stacks['1'].append(char) # append the next letter of the alphabet to the dictionary with key = '1'
                    print(new_stacks['1'])
                else:
                    new_stacks['1'] = [char] # otherwise this must be the first very first entry and we need to create that key value pair
                    print(new_stacks['1'])
            elif count > 2: # Let's now look at all other characters. They appear every 4 characters after the first letter in the string/line
                if (count - 2) % 4 == 0: # If the character placement is divisible by 4 (starting from character 2), then it's a letter of the alphabet
                    if str(int((count - 2) / 4) + 1) in new_stacks: # If that key exists...
                        new_stacks[str(int((count - 2) / 4) + 1)].append(char) # append the next letter to the dictionary
                        print(new_stacks[str(int((count - 2) / 4) + 1)])
                    else:
                        new_stacks[str(int((count - 2) / 4) + 1)] = [char] # otherwise this must be the first very first entry and we need to create that key value pair
                        print(new_stacks[str(int((count - 2) / 4) + 1)])

    print(new_stacks)

    # Remove all elements in the lists that are " " (space character)
    for row in new_stacks:
        while(" " in new_stacks[row]):
            new_stacks[row].remove(" ")

    print(new_stacks)

    moves = data[1].split("\n")
    print(moves)

    moves_list = []

    # Convert the moves string to a list with 3 indexes. each index will act as a move instruction
    # Index 0 will be how many items will be moved. Index 1 will be the list that we'll take items from
    # Index 2 will be where to move the items to
    for line in moves:
        line = re.findall('\d+', line)
        print(line)
        moves_list.append(line)

    print(moves_list)

    # Carry out the moves
    for row in moves_list:
        new_row = new_stacks[row[1]][:int(row[0])]
        # For part two this is the only change we need to make. Since the order remains the same, we don't need to reverse it.
        # new_row.reverse()
        new_stacks[row[2]] = new_row + new_stacks[row[2]]
        new_stacks[row[1]] = new_stacks[row[1]][int(row[0]):]
        print(new_stacks)

    print(new_stacks)

    string_with_top_values = ""

    # Print out the top values aka first element in the list
    for key in range(1, number_of_columns + 1):
        string_with_top_values = string_with_top_values + new_stacks[str(key)][0]

    print(string_with_top_values)