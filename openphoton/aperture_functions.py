import numpy as np
from scipy.special import jv

def rect(x):
    """rectangle function"""
    return abs(x) <= 0.5

def circ(r):
    """function for creating circular disk"""
    return abs(r) <= 1

def jinc(x):
    """jinc function that can handle zero division"""

    # sift nonzero elements of matrix x,
    # we do this to avoid division by zero
    mask = (x != 0)
    # initialize output with pi values
    out = np.pi*np.ones(np.shape(x))
    # compute bessel value for masked output values
    # np.divide() means element-wise division
    out[mask] = np.divide(jv(1,2 * np.pi*x[mask]), x[mask])
    return out