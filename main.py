# main.py
import numpy as np
import matplotlib.pyplot as plt

from parameters import L, alpha, N, NX
from initial_condition import f
from fourier import fourier_coefficients
from heat_solver import heat_solution

if __name__ == "__main__":
    # Spatial grid
    x = np.linspace(0, L, NX)

    # Fourier coefficients
    B = fourier_coefficients(f, L, N)

    # Time snapshots
    times = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05,0.06,0.07,0.08,0.09, 0.1,0.15,0.25,1]

    plt.figure(figsize=(8, 5))
    for t in times:
        u = heat_solution(x, t, L, alpha, B)
        plt.plot(x, u, label=f"t = {t}")

    plt.xlabel("Position x")
    plt.ylabel("Temperature u(x,t)")
    plt.title("1D Heat Equation (Dirichlet BCs) – Fourier Series")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
