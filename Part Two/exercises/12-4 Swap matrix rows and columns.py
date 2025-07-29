import numpy as np

def swap_rows(M, a, b):
    '''Swap the ath row and bth row of matrix M.'''
    # Type check
    if type(M) is not np.ndarray:
        try:
            M = np.array(M)
        except Exception as e:
            raise TypeError(f"Cannot convert to numpy array: {e}")
    # Validity check that a and b are valid row indices
    if not (0 <= a < M.shape[0]) or not (0 <= b < M.shape[0]):
        raise IndexError("Row indices out of bounds.")
    # Swap the rows
    M[[a, b]] = M[[b, a]]
    return M

def swap_columns(M, a, b):
    '''Swap the ath column and bth column of matrix M.'''
    # Type check
    if type(M) is not np.ndarray:
        try:
            M = np.array(M)
        except Exception as e:
            raise TypeError(f"Cannot convert to numpy array: {e}")
    # Validity check that a and b are valid column indices
    if not (0 <= a < M.shape[1]) or not (0 <= b < M.shape[1]):
        raise IndexError("Column indices out of bounds.")
    # Swap the columns
    M[:, [a, b]] = M[:, [b, a]]
    return M

# Tests
m = np.array([[0 , 1 , 2 , 3 , 4 , 5],
              [10, 11, 12, 13, 14, 15],
              [20, 21, 22, 23, 24, 25],
              [30, 31, 32, 33, 34, 35],
              [40, 41, 42, 43, 44, 45],
              [50, 51, 52, 53, 54, 55]
              ])

# Swap rows 1 and 3
swapped_rows = swap_rows(m.copy(), 1, 3)
print("Swapped Rows:\n", swapped_rows)

# Swap columns 2 and 4
swapped_columns = swap_columns(m.copy(), 2, 4)
print("Swapped Columns:\n", swapped_columns)