import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from figure_common import r_all

M = 40
by_norm, R = r_all(M)

ns, mn, mx, mean = [], [], [], []
for n in range(2, M + 1):
    vals = [R[alpha] for alpha in by_norm[n]]
    ns.append(n)
    mn.append(min(vals))
    mx.append(max(vals))
    mean.append(sum(vals) / len(vals))

plt.figure(figsize=(8, 5))
plt.plot(ns, mx, "o-", color="#1f3a93", label="max")
plt.plot(ns, mean, "s-", color="#16a085", label="mean")
plt.plot(ns, mn, "^-", color="#c0392b", label="min")
plt.xlabel(r"$N(\alpha)$")
plt.ylabel(r"$R(\alpha)$")
plt.title("Minimum, mean and maximum of R at each norm")
plt.legend()
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig("figures/fig_envelope.png", dpi=150)
plt.close()
print("wrote figures/fig_envelope.png")
