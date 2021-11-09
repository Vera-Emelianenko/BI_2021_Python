if __name__ == "__main__": 
    import numpy as np
    array1 = np.array([1.5,2.1,3.6,4.8,5.5,6.1,7.0,8.4,9.2,10.9])
    array2 = np.full((15, 10),0)
    array3 = np.arange(0,100,2.5)


def matrix_multiplication(a1,a2):
    if a1.shape[1] == a2.shape[0]:
        result = np.full((a1.shape[0], a2.shape[1]),0)
        for i in range(a1.shape[1]): 
            for j in range (a1.shape[1]): 
                result[i,j] = sum(a1[i,:]*a2[:,j])
        return result
    else:
        return None


def compute_2d_distance(a1,a2):
    # calculates distance between 2 points in 2 dimensions
    # a1, a2 - numpy arrays of shape (2,), a1 = ([x1,y1]), a2 = ([x2,y2])
    distance = ((a1[0] - a2[0]) ** 2 + (a1[1] - a2[1]) ** 2) ** 0.5
    return distance


def compute_multidimensional_distance(a1,a2):
    # calculates distance between 2 points in n dimensions
    # a1, a2 - numpy arrays of shape (n,), a1 = ([x1,y1,z1,...n2]), a2 = ([x2,y2,z2...n2])
    sum_of_squares = 0
    for i in range(len(a1)):
        sum_of_squares += (a1[i] - a2[i]) ** 2
    distance = sum_of_squares ** 0.5
    return distance