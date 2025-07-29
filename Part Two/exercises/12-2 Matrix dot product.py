import numpy as np

# Get some matricies

s1 = 2                                  # This is a scalar
m1 = np.array([[6, -9, 1], [4, 24, 8]]) # This is a 2 * 3 matrix
m2 = np.array([[1, 0], [0, 1]])         # This is a 2 * 2 identity matrix
m3 = np.array(([4, 3], [3, 2]))         # This is a 2 * 2 matrix
m4 = np.array([[-2, 3], [3, -4]])       # This is a 2 * 2 matrix

# Problem 1: s1 * m1
result1 = s1 * m1

# Problem 2: m2 * m1
result2 = m2 @ m1

# Problem 3: m3 * m4
result3 = m3 @ m4

# Print the results
print("Problem 1: s1 * m1 =\n", result1) # This is a 2 * 3 matrix
print("Problem 2: m2 * m1 =\n", result2) # This is a 2 * 3 matrix
print("Problem 3: m3 * m4 =\n", result3) # This is a 2 * 2 identity matrix. This means that m3 and m4 are inverses of each other.