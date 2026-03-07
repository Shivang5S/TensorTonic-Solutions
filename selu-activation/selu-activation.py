import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    # Write code here
    x = np.asarray(x, dtype = float)
    res = []

    for x0 in x:
        if x0 > 0:
            res.append(lam * x0)
        else:
            res.append(lam * alpha * (np.exp(x0) - 1))

    # converting res to np array, and rounding it to 4 digits
    res = np.asarray(res).round(4)
    return res
