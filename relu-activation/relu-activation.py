import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Creating an empty np array
    x = np.asarray(x)       # handles x as scalar, list, vector, matrix
    
    res = np.maximum(0, x)  # result array, with relu applied on x

    return res