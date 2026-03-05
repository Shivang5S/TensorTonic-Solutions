import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    rows = len(A)
    cols = len(A[0])

    res =[]
    for i in range(cols):
        phewphew =[]
        for j in range(rows):
            phewphew.append(A[j][i])
        res.append(phewphew)

    return np.array(res)