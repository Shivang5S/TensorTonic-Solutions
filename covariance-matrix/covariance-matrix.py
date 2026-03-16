import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X)
    if X.ndim != 2:
        return None
        
    N = len(X)
    if N < 2: 
        return None
        
    u = np.mean(X, axis = 0)
    X = X - u
    # That, above is broadcasting, np aligns shapes from the right

    return (X.T @ X)/(N - 1)

    