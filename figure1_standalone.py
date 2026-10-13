import os
from collections import defaultdict
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

def trace(q):
    return q[0]

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
by_norm = enumerate_hurwitz_by_norm(M)
ns, trs = [], []
for n in range(2, M + 1):
    for q in by_norm[n]:
        ns.append(n)
        trs.append(trace(q))
ns = np.array(ns)
trs = np.array(trs)
print(f"targets with 2 <= N <= {M}: {len(ns)}")

plt.figure(figsize=(8, 5))
plt.scatter(ns, trs, s=6, alpha=0.3, color="#1f3a93", edgecolors="none")
xx = np.linspace(2, M, 200)
plt.plot(xx, 2 * np.sqrt(xx), "--", color="#c0392b", label=r"$\pm 2\sqrt{N(\alpha)}$ (trace bound)")
plt.plot(xx, -2 * np.sqrt(xx), "--", color="#c0392b")
plt.xlabel(r"$N(\alpha)$")
plt.ylabel(r"$\mathrm{Tr}(\alpha)=2\,\mathrm{Re}(\alpha)$")
plt.title("Trace interval: every Hurwitz integer lies within the trace band")
plt.legend()
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig(os.path.join(FIG, "fig_trace_band.png"), dpi=150)
plt.close()
print("wrote", os.path.join(FIG, "fig_trace_band.png"))
