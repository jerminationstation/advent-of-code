elf_inventory = []
sum_list = []

# Convert input to list of lists aka elf_inventory
with open('pd_input.txt', 'r') as f:

    data = f.readlines()
    small_list = []
    count = 0

    for line in data:
        count+=1
        if line.strip(): # If line is empty
            small_list.append(int(line.strip('\n')))
            if count == len(data): # If this is last element in the list, append to the inventory list
                elf_inventory.append(small_list)
        else:
            elf_inventory.append(small_list)
            small_list = []
    print(elf_inventory)

for item in elf_inventory:
    each_elf_inventory_sum = sum(item)
    sum_list.append(each_elf_inventory_sum)

print(max(sum_list))