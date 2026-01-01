# solver.py
import numpy as np

def heat_solution(x, t, L, alpha, B):
    """
    Analytical solution of the 1D heat equation
    """
    u = np.zeros_like(x)

#summation of all sine modes with their decays and storing it in U array
    for n in range(1, len(B) + 1):
        u += (
            B[n-1]
            * np.sin(n * np.pi * x / L)
            * np.exp(-alpha * (n * np.pi / L)**2 * t)
        )
    return u