import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
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

def r3(N):
    if N < 0:
        return 0
    return sum(r2(N - x * x) for x in range(-int(N ** 0.5), int(N ** 0.5) + 1))

def nu(n, p):
    if n % 2 == 0:
        return r3(p - (n * n) // 4)
    return r3(4 * p - n * n)

def sigma_n(n, P):
    total = 0
    for p in range(2, P + 1):
        if isprime(p) and nu(n, p) > 0:
            total += nu(n, p)
    return total

N = 80
ns = list(range(2, N + 1))
vals = [sigma_n(n, n * n) for n in ns]

plt.figure(figsize=(8, 5))
plt.bar(ns, vals, color="#1f3a93", alpha=0.8)
plt.xlabel(r"$n$")
plt.ylabel(r"$\Sigma_n(n^2)$")
plt.title("Self-conjugate Goldbach decompositions of each real target")
plt.grid(alpha=0.25, axis="y")
plt.tight_layout()
plt.savefig("figures/fig_selfconj_count.png", dpi=150)
plt.close()
print("wrote figures/fig_selfconj_count.png")
