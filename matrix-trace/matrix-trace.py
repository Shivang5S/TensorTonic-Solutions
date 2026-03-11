import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    Sum = 0
    for i in range(len(A)):
        Sum += A[i][i]

    return Sum