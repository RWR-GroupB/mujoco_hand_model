# find the axis of the join given two points
import numpy as np

# the point pointint towards the arrow 
point1 = [14.2,-84.084,-8.617]

# the second point which acts as the base of the arrow
point2 = [14.2,-107.51,-18.434]

point1 = np.array(point1)
point2 = np.array(point2)

# the vector pointing from point2 to point1
vector = point1 - point2
print("vector: ", vector/1000)

# axis point
axis_point = point2 + vector/2
print("axis point: ", axis_point/1000)