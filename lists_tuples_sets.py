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
