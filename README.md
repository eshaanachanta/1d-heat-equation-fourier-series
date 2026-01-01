# 1D Heat Equation — Fourier Series Solution

This project shows how Fourier analysis can be used to understand heat diffusion in a 1D rod.  
An initial temperature curve is broken into simpler sine waves, each of which evolves independently over time.  
The combined contribution of each mode explains how temperature spreads and smooths out over time.

---

## Core Idea

- Break the initial temperature curve into sine wave modes  
- Analyze how each mode decays over time  
- Reconstruct the full temperature distribution using a finite number of modes  

---

## Mathematical Model

The partial differential equation that governs heat flow in a 1D rod is:

$$\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}$$


---

## Boundary Conditions

We use Dirichlet boundary conditions:

$$
u(0,t) = u(L,t) = 0
$$

---

## Initial Condition

$$
u(x,0) = f(x)
$$

---

## Fourier Series Solution

$$
u(x,t) =
\sum_{n=1}^{\infty}
B_n
\sin\left(\frac{n\pi x}{L}\right)
e^{-\alpha\left(\frac{n\pi}{L}\right)^2 t}
$$

---

The Fourier sine coefficients \(B_n\) are given by:

$$
B_n = \frac{2}{L} \int_0^L f(x) \, \sin\left(\frac{n \pi x}{L}\right) \, dx
$$

These coefficients represent the **contribution of each sine wave** to the initial temperature profile.  
The decay of each sine mode over time is given by:

$$
e^{-\alpha \left(\frac{n \pi}{L}\right)^2 t}
$$


## Output

The program plots the temperature distribution along the rod at multiple time snapshots.  
These plots illustrate how heat diffuses and how temperature variations smooth out over time.

![image_alt](https://github.com/eshaanachanta/1d-heat-equation-fourier-series/blob/main/Heat%20Diffusion%20Illustration.png?raw=true)

---

## How to Run

```bash
python main.py


Make sure you have:
-Python 3.11+
-NumPy
-Matplotlib

