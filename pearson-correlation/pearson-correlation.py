import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    # Write code here
    if len(X) < 2:
        return None
        
    X = np.asarray(X)
    if X.ndim != 2:
        return None
        
    sig = np.std(X, axis = 0, ddof = 1) # If axis is not specified, it returns a scalar, that is for complete X. But we want it per attribute.
    # ddof - delta degrees of freedom
    
    return np.cov(X.T)/np.outer(sig, sig)