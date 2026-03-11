import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.asarray(x)
    x = x - x.max(axis = -1, keepdims = True)
    e = np.exp(x)
    return e/e.sum(axis = -1, keepdims = True)

    # keepdims=True — keep the collapsed axis as size 1 instead of dropping it