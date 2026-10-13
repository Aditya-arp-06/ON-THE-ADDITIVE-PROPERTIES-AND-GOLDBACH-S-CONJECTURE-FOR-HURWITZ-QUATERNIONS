import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from figure_common import r_all

M = 40
by_norm, R = r_all(M)

ns, rvals = [], []
for n in range(2, M + 1):
    for alpha in by_norm[n]:
        ns.append(n)
        rvals.append(R[alpha])

plt.figure(figsize=(8, 5))
plt.scatter(ns, rvals, s=6, alpha=0.35, color="#1f3a93", edgecolors="none")
plt.xlabel(r"$N(\alpha)$")
plt.ylabel(r"$R(\alpha)$")
plt.title("The quaternion Goldbach comet")
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig("figures/fig_comet.png", dpi=150)
plt.close()
print("wrote figures/fig_comet.png")
