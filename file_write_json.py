import json

points_3D = [[1, 2, 4], [2, 4, 3], [0, 0, 1], [5, 4, 0]]
my_dict2 = {'Jan': 31, 'Feb': 28, 'Mar': 31}

my_file = 'hello_out.json'
# w - write (text)
with open(my_file, 'w') as f:
    json.dump(my_dict2, f)