import numpy as np
if __name__ == "__main__":
    # create 3 arrays in np
    # first array - from python object
    array1 = np.array([1.5, 2.1, 3.6, 4.8, 5.5, 6.1, 7.0, 8.4, 9.2, 10.9])
    # second array - using .full function 
    array2 = np.full((15, 10), 0)
    # third array  - using arrange
    array3 = np.arange(0, 100, 2.5)


def matrix_multiplication1(a1, a2):
    """Multiplies two matrices

    Parameters:
    argument1,2 (np array): matrices to be multiplied

    Returns:
    numpy array if matrices can be multiplied, None if they can't
    """
    if a1.shape[1] == a2.shape[0]:
        result = np.zeros((a1.shape[0], a2.shape[1]))
        for i in range(a1.shape[1]):
            for j in range(a2.shape[0]):
                result[i, j] = sum(a1[i, :]*a2[:, j])
        return result
    else:
        return None


def matrix_multiplication(a1, a2):
    """Multiplies two matrices using numpy.matmul() function

    Parameters:
    argument1,2 (np array): matrices to be multiplied

    Returns:
    numpy array if matrices can be multiplied, None if they can't
    """
    if a1.shape[1] == a2.shape[0]:
        result = np.matmul(a1, a2)
        return result
    else:
        return None


def multiplication_check(list_of_matrices):
    """Checks if matrices can be multiplied in the given order

    Parameters:
    argument1 (list of np arrays): matrices to be multiplied

    Returns:
    bool: True if matrices can be multiplied, False if they can't
    """
    for i in range (1, len(list_of_matrices)):
        if list_of_matrices[i-1].shape[1] != list_of_matrices[i].shape[0]:
            return False
    return True


def multiply_matrices(list_of_matrices):
    """Checks if matrices can be multiplied in the given order and multiplies them

    Parameters:
    argument1 (list of np arrays): matrices to be multiplied

    Returns:
    Result of matrix multiplication if matrices can be multiplied, None if they can't
    """
    if multiplication_check(list_of_matrices):
        res = list_of_matrices[0]
        for i in range (1, len(list_of_matrices)):
            res = np.matmul(res, list_of_matrices[i])
        return res
    else:
        return None


def compute_2d_distance(a1, a2):
    """Calculates distance between 2 points in 2 dimensions

    Parameters:
    a1, a2 - numpy arrays of shape (2,), a1 = ([x1,y1]), a2 = ([x2,y2])

    Returns:
    float: 2d distance between 2 points
    """
    distance = ((a1[0] - a2[0]) ** 2 + (a1[1] - a2[1]) ** 2) ** 0.5
    return distance


def compute_multidimensional_distance(a1, a2):
    """Calculates distance between 2 points in n dimensions

    Parameters:
    a1, a2 - numpy arrays of shape (n,), a1 = ([x1,y1,z1,...n2]), a2 = ([x2,y2,z2...n2])

    Returns:
    float: nd-distance between 2 points
    """
    sum_of_squares = 0
    for i in range(len(a1)):
        sum_of_squares += (a1[i] - a2[i]) ** 2
    distance = sum_of_squares ** 0.5
    return distance
