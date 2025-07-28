import numpy as np

v = np.array([2., 2., 4.])

# project vector onto 3d
e1 = np.array([1., 0., 0.])
e2 = np.array([0., 1., 0.])
e3 = np.array([0., 0., 1.])
v1 = np.dot(v, e1) * e1
v2 = np.dot(v, e2) * e2
v3 = np.dot(v, e3) * e3

# prints out the magnitude of projection:
print(np.linalg.norm(v1))
print(np.linalg.norm(v2))
print(np.linalg.norm(v3))