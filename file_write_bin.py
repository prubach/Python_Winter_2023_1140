import _pickle

points_3D = [[1, 2, 4], [2, 4, 3], [0, 0, 1], [5, 4, 0]]

my_file = 'hello_out.dat'
# wb - write binary
with open(my_file, 'wb') as f:
    _pickle.dump(points_3D, f)