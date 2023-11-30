num_list = [2, 7, 5, 15, 7, 9, 11, 5, 13, 18]
num_list_pow = [ x**2 for x in num_list]
print(num_list_pow)
num_list_pow_sorted = sorted(num_list_pow)
print(num_list_pow_sorted)
num_list_pow_sorted_rev = sorted(num_list_pow, reverse=True)
print(num_list_pow_sorted_rev)
print('--- set ------')
num_list_pow_set = set(num_list_pow)
print(num_list_pow_set)

num_list_pow_unique = sorted(list(set(num_list_pow)))
print(num_list_pow_unique)

print('--- tuples ------')
tuple_list = [(1, 2), (2, 4), (0, 0), (5, 4)]
x, y = tuple_list[0]
print(x, y)
t = (1, 5, 6)
print(t[1])
# Error below
#t[1] = 6
print(t[1])

print('--- matrix ------')

list_2D = [[1, 2, 4], [2, 4, 3], [0, 0, 1], [5, 4, 0]]
#print(list_2D)

for row in list_2D:
    print(row)
print()
#TODO:
# 1. Sum each row of the matrix - create a list of those sums
row_sum = []
for row in list_2D:
    row_sum.append(sum(row))
print(row_sum)
# 2. Sum all elements
print(sum(row_sum))
# 3. Sum each column of the matrix - create a list of those sums
col_sum = [0, 0, 0]
for row in list_2D:
    for i in range(len(row)):
        col_sum[i] += row[i]
print(col_sum)


# Summe der Zeile
transposed_matrix = list(zip(*list_2D))
column_sums = [sum(column) for column in transposed_matrix]

print(transposed_matrix)
print(column_sums)

print('--------------')

lang_name = ['Python', 'Java', 'C++']
lang_vers = ['3.12', '17', '14']

lang_names_vers = list(zip(lang_name, lang_vers))
print(lang_names_vers)
