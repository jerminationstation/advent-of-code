current_dir = []
all_folders = {}
current_index = 0

with open('pd_input.txt', 'r') as f:

    data = f.readlines()

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
    

    # This is the only change for part 2. Pretty straight forward
    space_used = all_folders['/']
    free_space = 70000000 - space_used
    space_needed = 30000000 - free_space
    potential_folders_to_delete = []
             
    for key in all_folders:
        if all_folders[key] > space_needed:
            potential_folders_to_delete.append(all_folders[key])
    
    folder_to_delete = min(potential_folders_to_delete)

    print(folder_to_delete)

            

