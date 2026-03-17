import numpy as np
from scipy.special import erf

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    w, g, s = np.asarray(w, dtype = float), np.asarray(g, dtype = float), np.asarray(s, dtype = float)
    s = beta * s + (1 - beta) * (g ** 2)
    w = w - ((lr * g)/np.sqrt(s + eps))
    return w, s