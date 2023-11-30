points_2D = [(1, 2), (2, 4), (0, 0), (5, 4)]

import matplotlib.pyplot as plt
xs = [i[0] for i in points_2D]
ys = [i[1] for i in points_2D]

plt.plot(xs, ys, '^')
plt.xlabel('x')
plt.ylabel('y')
#plt.show()
plt.savefig('points2D.png')









points_3D = [[1, 2, 4], [2, 4, 3], [0, 0, 1], [5, 4, 0]]
