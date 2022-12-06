strategy_list = []
result_list = []
score_chart = {'AX': 4, 'AY': 8, 'AZ': 3, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 7, 'CY': 2, 'CZ': 6}

with open('pd_input.txt', 'r') as f:

    data = f.readlines()

    for line in data:
        line = line.strip("\n").split(" ")
        strategy_list.append(line)

for item in strategy_list:
    round_result = ''.join(item)
    result_list.append(score_chart[round_result])

print(sum(result_list))