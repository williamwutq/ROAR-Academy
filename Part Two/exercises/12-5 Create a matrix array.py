import numpy as np

def set_array(L, rows, cols, order = 'C'):
    """
    Create a matrix array from a list of lists.
    
    Parameters:
    L (list): The input list to convert into a matrix. Must have a length equal to rows * cols.
    rows (int): The number of rows in the matrix.
    cols (int): The number of columns in the matrix.
    order (str): The order in which to fill the matrix ('R' for row-major, 'C' for column-major).
    
    Returns:
    np.ndarray: A numpy array representing the matrix.
    """
    # Type check and value check for the input list
    if type(L) is not list:
        raise TypeError("Input must be a list")
    if type(rows) is not int or type(cols) is not int:
        raise TypeError("Rows and columns must be integers")
    if rows <= 0 or cols <= 0:
        raise ValueError("Rows and columns must be positive integers")
    if len(L) != rows * cols:
        raise ValueError("Length of list must be equal to rows * cols")
    
    if (order == 'R'):
        # Create a row-major matrix
        return np.array(L).reshape((rows, cols), order='C')
    elif (order == 'C'):
        # Create a column-major matrix
        return np.array(L).reshape((rows, cols), order='F')
    else:
        raise ValueError("Order must be 'R' for row-major or 'C' for column-major")
    
# Tests
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(set_array(L, 3, 4, 'R'))  # Row-major order
print(set_array(L, 3, 4, 'C'))  # Column-major order
print(set_array(L, 2, 6, 'R'))  # Row-major order
print(set_array(L, 6, 2, 'C'))  # Column-major order
try:
    print(set_array(L, 6, 3, 'R'))  # This should fail
except ValueError as e:
    print(e)