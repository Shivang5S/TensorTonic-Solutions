import numpy as np
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    res = []
    # Since, the question demands to return a list, and the input itself is a list. Also, x is not a vector (np array), we may simply use ternary operator element wise. Because np.where is useful for eliminating the loops in np arrays
    for x0 in x:
        res.append(np.where(x0 > 0, x0, alpha * (np.exp(x0) - 1)))
    
    return res