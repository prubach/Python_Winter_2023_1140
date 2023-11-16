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

#TODO:
# 1. Sum each row of the matrix - create a list of those sums
# 2. Sum all elements
# 3. Sum each column of the matrix - create a list of those sums