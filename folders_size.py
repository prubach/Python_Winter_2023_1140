#TODO for a given folder list only regular files and sum
# the size of all
import os

my_folder = 'C:\Temp'

print(os.listdir(my_folder))
# Solution by Julia Kubisa
a = sum(os.path.getsize(os.path.join(my_folder, f))
        for f in os.listdir(my_folder) if os.path.isfile(os.path.join(my_folder, f)))
#print(os.listdir('.'))
print(f'total size: {a}')

#TODO sum all sizes of files in a given folder including the subfolders and their subfolders etc.

# contributed by Jakub Targalski
def folder_size(folder):
    total_size = 0
    for f in os.listdir(folder):
        file_path = os.path.join(folder, f)
        if os.path.isfile(file_path):
            total_size += os.path.getsize(file_path)
        elif os.path.isdir(file_path):
            total_size += folder_size(file_path)
    return total_size

print(f'Total size of all files in the folder is {folder_size(my_folder)}.')