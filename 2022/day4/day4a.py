assignment_pairs = []

with open('pd_input.txt', 'r') as f:

    data = f.readlines()

    for line in data:
        line = line.strip('\n').split(',')

        new_line = []

        for item in line:
            item = item.split('-')
            item = range(int(item[0]),int(item[1]) + 1)
            item = set(item)
            new_line.append(item)
        
        assignment_pairs.append(new_line)

print(assignment_pairs)

count = 0

for row in assignment_pairs:
    if row[0].issubset(row[1]) or row[1].issubset(row[0]):
        count += 1

print(count)