import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    x = np.asarray(x)
    res = []

    for x0 in x:
        if x0 >= 0:
            res.append(x0)
        else:
            res.append(alpha * x0)

    res = np.asarray(res)
    return res