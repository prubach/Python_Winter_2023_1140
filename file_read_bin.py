import _pickle

my_file = 'hello_out.dat'
# rb - read binary
with open(my_file, 'rb') as f:
    points = _pickle.load(f)
    print(points)
    print(points[1][1])