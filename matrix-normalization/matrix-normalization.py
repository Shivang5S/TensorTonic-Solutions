import numpy as np

def matrix_normalization(matrix, axis = None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here
    matrix = np.asarray(matrix, dtype = float)

    if matrix.ndim != 2:
        return None
    
    if axis is not None and (axis < 0 or axis >= matrix.ndim):
        return None
        
    res = 0
    if norm_type == 'l1':
        # Manhattan Dist
        res = np.abs(matrix).sum(axis = axis, keepdims = True)
        # keepdims is only used when we will use the array further somewhere, and its broadcasting may help

    elif norm_type == 'l2':
        # Euclidean Dist
        res = np.sqrt(np.sum(matrix**2, axis = axis, keepdims = True))

    elif norm_type == 'max':
        # Infinity
        res = np.max(matrix, axis = axis, keepdims = True)
    
    else:
        return None

    res = np.asarray(res)
    res = np.where(res == 0, 1, res)
    
    return matrix/res