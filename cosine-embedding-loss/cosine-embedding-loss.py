import numpy as np

def norm(x):
    return np.sqrt(np.sum(x ** 2))

def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    x1, x2 = np.asarray(x1, dtype = float), np.asarray(x2, dtype = float)
    
    cosi = (x1 @ x2)/(norm(x1) * norm(x2))

    if label > 0:
        return float(1 - cosi)
    else:
        return float(max(0, cosi - margin))
