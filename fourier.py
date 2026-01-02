import numpy as np

def fourier_coefficients(f, L, N, nx=10000):

    #Calculates the  Fourier sine coefficients using  integration

    B = np.zeros(N) #empty array to store the coefficients
    x = np.linspace(0, L, nx) #creates an array which will act as our rod
    fx = f(x)

    #this is the integration process
    dx = x[1] - x[0]

    for n in range(1, N + 1):
        y = fx * np.sin(n * np.pi * x / L)
        B[n-1] = (2 / L) * (np.sum(y) - 0.5*(y[0] + y[-1])) * dx   #stores the coefficient value in the array

    return B
