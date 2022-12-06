with open('pd_input.txt', 'r') as f:

    data = f.read()
    count = 0
    pattern_length = 4

    for char in data:
        count += 1
        if count >= pattern_length:
            string_to_compare = ""
            for my_char in data[count - pattern_length:count]:
                if my_char not in string_to_compare:
                    string_to_compare += my_char
            if string_to_compare == data[count - pattern_length:count]:
                print(count)
                break
