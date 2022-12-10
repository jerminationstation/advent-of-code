# STEP 1: Find all directories/sub-directories
# STEP 2: Find the size of all the directories
# STEP 3: Find sum of all directories less than 10000

# We meed to create keys for a dictionary
# The key will be represented by each unique folder name.
# So each key name will tell us the "nesting" in a  sense. E.g. Folder1-folder2-folder3 etc. as the name of the key
# If it's a long nested folder, then the name will be quite long, but it will work for this challenge

# While we search we need to keep track of which folder we are in by using a list. This will help us with the 'cd ..' and the 'cd xyz'
# If we see a 'cd xyz', then we add to our list
# If we see 'cd ..' then we remove last entry in our list
# Search for next '$ ls', then use the list above to see which folder we are in (list[-1] for last element if we are appending to end of list).
# As directories are explored ( by 'ls'), store data in dictionary with directory name as key. This name will be based on the strings in the list (separated by '-' using a join method maybe)
# The value will be the sum of the file sizes
# We will need to search for each line with a file. These are the lines that don't start with '$'.
# However, if it starts with 'dir' it's a folder and we can ignore
# So if no '$' and no 'dir', then it's a file and we can add that the value to the 'size' (we can use the split string method) of our current folder
# Then we add the size to each parent folder above.
# If we 'cd' into another directory, then update/append directory name to our list


current_dir = []
all_folders = {}
current_index = 0

with open('pd_input.txt', 'r') as f:

    data = f.readlines()
    # STEP 1
    for row in data:
        # Update current_dir list when new directory discovered aka 'cd xyz'
        if row.startswith('$ cd') and row != '$ cd ..\n':
            current_dir.append(row.split(' ')[2].strip('\n'))
            directory_name = '-'.join(current_dir)
            # Update all_folders list with newly found directory
            if directory_name not in all_folders:
                all_folders[directory_name] = 0
        # If 'cd ..' then we need to move up to the parent directory by removing last element in our current_dir list
        elif row == '$ cd ..\n':
            current_dir = current_dir[:-1]
        #STEP 2
        # Let's check the row if it's a file. These won't start with $. We can ignore lines with dir since they don't really cause us to do anything
        elif not row.startswith('$') and not row.startswith('dir'):
            # Get current directory name
            directory_name = '-'.join(current_dir)
            # Find file size
            file_size = int(row.split(' ')[0].strip('\n'))
            # Add file size to the current size
            all_folders[directory_name] += file_size
            # Update size of upper level folders
            upper_level_folders_count = len(directory_name.split('-')[:-1])
            next_upper_directory = '-'.join(directory_name.split('-')[:-1])
            # Let's update the folder size of each parent folder. We do this by manipulating the folder/directory names.
            # That is, removing the last folder name from the end of the string
            while upper_level_folders_count != 0:     
                all_folders[next_upper_directory] += file_size
                next_upper_directory = '-'.join(next_upper_directory.split('-')[:-1])
                upper_level_folders_count -= 1
    # STEP 3
    total = 0                  
    for key in all_folders:
        if all_folders[key] < 100000:
            total += all_folders[key]

    print(total)

            

