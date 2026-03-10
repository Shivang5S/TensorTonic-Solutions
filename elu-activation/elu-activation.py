import numpy as np
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    res = []
    for x0 in x:
        res.append(np.where(x0 > 0, x0, alpha * (np.exp(x0) - 1)))
    
    return res