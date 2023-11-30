import pandas as pd
import plotly.express as px

points_2D = [(1, 2), (2, 4), (0, 0), (5, 4)]
df = pd.DataFrame(points_2D, columns=['x', 'y'])
#print(df)
fig = px.scatter(df, x='x', y='y')
fig.show()

points_3D = [[1, 2, 4], [2, 4, 3], [0, 0, 1], [5, 4, 0]]
df3 = pd.DataFrame(points_3D, columns=['x', 'y', 'z'])
#print(df)
fig = px.scatter_3d(df3, x='x', y='y', z='z')
fig.show()
