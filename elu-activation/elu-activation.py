import numpy as np
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    res = []
    for x0 in x:
        if x0 > 0:
            res.append(x0)

        else:
            res.append(alpha * (np.exp(x0) - 1))

    return res