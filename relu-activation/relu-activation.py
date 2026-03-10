import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    '''
    Requirements are:
        Return result using NumPy (not Python lists)
        Handle scalar, list, and NumPy array inputs
        Fully vectorized (no explicit Python loops)
        Preserve input shape
    '''
    x = np.asarray(x)       # handles x as scalar, list, vector, matrix
    
    return np.where(x <= 0, 0, x)