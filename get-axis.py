# find the axis of the join given two points
import numpy as np

# the point pointint towards the arrow 
point1 = [83.20,-101.314,-5.536]

# the second point which acts as the base of the arrow
point2 = [83.20,-93.97,-23.06]

point1 = np.array(point1, dtype=np.float64)
point2 = np.array(point2, dtype=np.float64)

# the vector pointing from point1 to point2
vector = point2 - point1
vector_u = vector/np.linalg.norm(vector)
print("vector: ", vector_u)

# axis point
axis_point = point1 + vector/2
print("axis point: ", axis_point/1000)