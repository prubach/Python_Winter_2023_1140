my_file = 'numbers.csv'
with open(my_file, 'r') as f:
    lines = f.readlines()
    i = 0
    for line in lines:
        i += 1
        print(f'{i}: {line}', end='')

#TODO
# Read the content into a 2D list (matrix) and then sum up the rows, cols and all