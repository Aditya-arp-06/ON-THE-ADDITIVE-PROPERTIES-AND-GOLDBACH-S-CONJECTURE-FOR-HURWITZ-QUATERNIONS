import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sympy import isprime

def r2(m):
    if m == 0:
        return 1
    d1 = d3 = 0
    for d in range(1, int(m ** 0.5) + 1):
        if m % d == 0:
            for dd in {d, m // d}:
                r = dd % 4
                if r == 1:
                    d1 += 1
                elif r == 3:
                    d3 += 1
    return 4 * (d1 - d3)

def three_squares(N):
    if N < 0:
        return []
    return [x for x in range(-int(N ** 0.5), int(N ** 0.5) + 1)
            if r2(N - x * x) > 0]

def smallest_p(n):
    if n % 2 == 1:
        p = 3
        while True:
            if 4 * p > n * n and three_squares(4 * p - n * n):
                return p
            p += 2
            while not isprime(p):
                p += 2
    else:
        m = n // 2
        p = 2
        while True:
            if p > m * m and isprime(p) and three_squares(p - m * m):
                return p
            p += 1

N = 120
even_n, even_p = [], []
odd_n, odd_p = [], []
for n in range(2, N + 1):
    if n % 2 == 0:
        even_n.append(n)
        even_p.append(smallest_p(n))
    else:
        odd_n.append(n)
        odd_p.append(smallest_p(n))

plt.figure(figsize=(8, 5))
plt.scatter(even_n, even_p, s=14, color="#1f3a93", label="even n")
plt.scatter(odd_n, odd_p, s=14, color="#c0392b", label="odd n")
xx = np.linspace(2, N, 200)
plt.plot(xx, xx * xx / 4, "--", color="black", label=r"$p=n^2/4$")
plt.xlabel(r"$n$")
plt.ylabel(r"smallest prime $p$ with $n=\pi+\bar\pi$")
plt.title("Real-axis Goldbach: smallest valid prime for each n")
plt.legend()
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig("figures/fig_realaxis_minprime.png", dpi=150)
plt.close()
print("wrote figures/fig_realaxis_minprime.png")

# ---------------------------------------------------------------------
# Terminal output:  python fig13.py
# ---------------------------------------------------------------------
# wrote figures/fig_realaxis_minprime.png
