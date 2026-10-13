import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from figure_common import r_all

M = 40
by_norm, R = r_all(M)

ns, mn = [], []
for n in range(2, M + 1):
    vals = [R[alpha] for alpha in by_norm[n]]
    ns.append(n)
    mn.append(min(vals))

ns = np.array(ns)
mn = np.array(mn)
slope, intercept = np.polyfit(ns, mn, 1)

plt.figure(figsize=(8, 5))
plt.plot(ns, mn, "o", color="#1f3a93")
plt.plot(ns, intercept + slope * ns, "--", color="#c0392b",
         label=f"linear fit: slope {slope:.1f}")
plt.xlabel(r"$N(\alpha)$")
plt.ylabel(r"$\min R(\alpha)$ at each norm")
plt.title("Lower envelope of the representation count")
plt.legend()
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig("figures/fig_Rmin_fit.png", dpi=150)
plt.close()
print("wrote figures/fig_Rmin_fit.png, slope =", round(slope, 1))
