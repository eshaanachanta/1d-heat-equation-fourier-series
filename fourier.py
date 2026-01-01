# fourier.py
import numpy as np

def fourier_coefficients(f, L, N, nx=10000):

    #Compute Fourier sine coefficients using numerical integration

    B = np.zeros(N)
    x = np.linspace(0, L, nx)
    fx = f(x)
    dx = x[1] - x[0]

    for n in range(1, N + 1):
        y = fx * np.sin(n * np.pi * x / L)
        B[n-1] = (2 / L) * (np.sum(y) - 0.5*(y[0] + y[-1])) * dx

    return B