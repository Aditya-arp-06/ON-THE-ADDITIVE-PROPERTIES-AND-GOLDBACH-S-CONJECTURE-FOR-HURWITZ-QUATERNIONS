import os
from collections import defaultdict, Counter
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "figures")
os.makedirs(FIG, exist_ok=True)

def is_hurwitz(q):
    A, B, C, D = q
    return len({A & 1, B & 1, C & 1, D & 1}) == 1

def norm(q):
    A, B, C, D = q
    return (A * A + B * B + C * C + D * D) // 4

def sub(q1, q2):
    return (q1[0] - q2[0], q1[1] - q2[1], q1[2] - q2[2], q1[3] - q2[3])

def make_prime_sieve(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return sieve

def enumerate_hurwitz_by_norm(nmax):
    by_norm = defaultdict(list)
    R = int((4 * nmax) ** 0.5) + 1
    for A in range(-R, R + 1):
        a2 = A * A
        if a2 > 4 * nmax:
            continue
        for B in range(-R, R + 1):
            b2 = a2 + B * B
            if b2 > 4 * nmax:
                continue
            for C in range(-R, R + 1):
                c2 = b2 + C * C
                if c2 > 4 * nmax:
                    continue
                for D in range(-R, R + 1):
                    s = c2 + D * D
                    if s > 4 * nmax or s % 4 != 0:
                        continue
                    q = (A, B, C, D)
                    if is_hurwitz(q):
                        by_norm[s // 4].append(q)
    return by_norm

M = 40
NORMS = [18, 27, 36]
by_norm = enumerate_hurwitz_by_norm(M)
sieve = make_prime_sieve(4 * M + 10)
prime_points = {p: pts for p, pts in by_norm.items() if p >= 2 and sieve[p]}

def r_of(alpha, n):
    R = 0
    for p, pts in prime_points.items():
        if p > n:
            continue
        for pi in pts:
            p2 = norm(sub(alpha, pi))
            if p2 < len(sieve) and sieve[p2]:
                R += 1
    return R

dist = {}
for n in NORMS:
    vals = [r_of(alpha, n) for alpha in by_norm[n]]
    dist[n] = Counter(vals)
    print(f"N={n}: {len(vals)} targets, R values {sorted(dist[n].items())}")

plt.figure(figsize=(8, 5))
for nn, col in [(18, "#1f3a93"), (27, "#16a085"), (36, "#c0392b")]:
    xs = sorted(dist[nn])
    plt.bar(xs, [dist[nn][x] for x in xs], width=25, alpha=0.75, color=col,
            label=f"$N(\\alpha)={nn}$", edgecolor="black", linewidth=0.5)
    for x in xs:
        plt.text(x, dist[nn][x] + 6, str(dist[nn][x]),
                 ha="center", va="bottom", fontsize=8)
plt.xlabel(r"$R(\alpha)$")
plt.ylabel(r"number of $\alpha$")
plt.title(r"Distribution of $R(\alpha)$ at fixed norm: one bar per unit-orbit class")
plt.legend()
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig(os.path.join(FIG, "fig_R_distribution.png"), dpi=150)
plt.close()
print("wrote", os.path.join(FIG, "fig_R_distribution.png"))
