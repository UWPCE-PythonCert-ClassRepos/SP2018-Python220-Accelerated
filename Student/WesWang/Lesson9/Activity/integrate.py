def f(x):
    return x**2


def integrate(f, a, b, N):
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx


def integrate_f_with_functional_tools(f, a, b, N):
    dx = (b - a) / N
    return sum(map(f, ((a + y * dx) for y in range(N)))) * dx


import numpy as np

def integrate_numpy(f, a, b, N):
    dx = (b - a) / N
    i = np.arange(N)
    s = np.sum(f(a + (i * dx)))
    return s * dx