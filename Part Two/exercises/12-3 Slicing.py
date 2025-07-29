import numpy as np

m = np.array([[0 , 1 , 2 , 3 , 4 , 5],
              [10, 11, 12, 13, 14, 15],
              [20, 21, 22, 23, 24, 25],
              [30, 31, 32, 33, 34, 35],
              [40, 41, 42, 43, 44, 45],
              [50, 51, 52, 53, 54, 55]
              ])

# Do the silicing
s1 = m[1, 2:4]    # Extracts elements from row 1, columns 2 to 3
s2 = m[2:4, 4:6]  # Extracts elements from rows 2 to 3, columns 4 to 5
s3 = m[:, 1]      # Extracts all rows, column 1
s4 = m[2::2, ::2] # Extracts every second row starting from row 2, every second column starting from column 2

# Print the results
print("s1:", s1, "shape:", s1.shape)
print("s2:", s2, "shape:", s2.shape)
print("s3:", s3, "shape:", s3.shape)
print("s4:", s4, "shape:", s4.shape)