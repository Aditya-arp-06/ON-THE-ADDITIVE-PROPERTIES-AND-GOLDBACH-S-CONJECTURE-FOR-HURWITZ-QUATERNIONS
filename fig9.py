import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from figure_common import r_all

M = 40
by_norm, R = r_all(M)

ns, rvals = [], []
for n in range(2, M + 1):
    for alpha in by_norm[n]:
        ns.append(n)
        rvals.append(R[alpha])

ln = np.log(ns)
lr = np.log(rvals)
slope, intercept = np.polyfit(ln, lr, 1)

plt.figure(figsize=(8, 5))
plt.scatter(ln, lr, s=6, alpha=0.35, color="#1f3a93", edgecolors="none")
plt.plot(ln, intercept + slope * ln, "--", color="#c0392b",
         label=f"fit: slope {slope:.2f}")
plt.xlabel(r"$\log N(\alpha)$")
plt.ylabel(r"$\log R(\alpha)$")
plt.title("Representation count on logarithmic axes")
plt.legend()
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig("figures/fig_R_loglog.png", dpi=150)
plt.close()
print("wrote figures/fig_R_loglog.png, slope =", round(slope, 3))
