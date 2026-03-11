import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x, y = np.asarray(x, dtype = float), np.asarray(y, dtype = float)

    return float(np.abs(y - x).sum())
    