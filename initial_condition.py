# initial_condition.py
import numpy as np
from parameters import L

def f(x):
    """
    Initial temperature distribution u(x,0)
    """
    return 100*np.sin(np.pi * x / L)