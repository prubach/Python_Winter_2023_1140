my_file = 'numbers.csv'
with open(my_file, 'r') as f:
    lines = f.readlines()
    i = 0
    for line in lines:
        i += 1
        print(f'{i}: {line}', end='')

#TODO
# Read the content into a 2D list (matrix) and then sum up the rows, cols and all
print('\n')

list_2D = []

for line in lines:
    els = line.strip().split(';')
    els_int = [int(el) for el in els]
    list_2D.append(els_int)

print(list_2D)
#
# el1 = lines[0].strip().split(';')
# el2 = lines[1].strip().split(';')
# el3 = lines[2].strip().split(';')
#
# for n in range(0, len(el1)):
#     el1[n] = int(el1[n])
#     el2[n] = int(el2[n])
#     el3[n] = int(el3[n])

#list_2D = [el1, el2, el3]

row_sum = []
for row in list_2D:
    row_sum.append(sum(row))
print(f'Sum of rows is {row_sum}')

col_sum = [0, 0, 0]
for row in list_2D:
    for i in range(len(row)):
        col_sum[i] += row[i]

print(f'Sum of columns is {col_sum}')
print(f'Sum of all is {sum(row_sum)}')