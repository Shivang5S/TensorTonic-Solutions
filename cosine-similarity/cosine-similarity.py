import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    def norm(a):
        return np.sqrt(np.sum(a**2))

    a, b = np.asarray(a, dtype = float), np.asarray(b, dtype = float)

    if norm(a) == 0 or norm(b) == 0:
        return a @ b
        
    return (a @ b) / (norm(a) * norm(b))