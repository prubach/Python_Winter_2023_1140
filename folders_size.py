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