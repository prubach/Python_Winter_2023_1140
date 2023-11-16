import math

num_list = [2, 5, 7, 9, 11, 13, 18]

'''
TODO 
1. Print the subsequent 2nd powers of elements in the list
2. Sum the 2nd powers of elements of the list
'''

a = 7

#print(a*a)
#print(a**2)
#print(math.pow(a, 2))

for el in num_list:
    print(el**2)

sum_els = 0
for el in num_list:
    sum_els = sum_els + el ** 2
print(f'Sum: {sum_els}')

######
print('----------------------')
num_list_pow = [ x**2 for x in num_list]
print(num_list_pow)
print(sum(num_list_pow))

