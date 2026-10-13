import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from figure_common import enumerate_hurwitz_by_norm, sigma_odd

M = 40
by_norm = enumerate_hurwitz_by_norm(M)
ns = list(range(1, M + 1))
counts = [len(by_norm[n]) for n in ns]
predicted = [24 * sigma_odd(n) for n in ns]

plt.figure(figsize=(8, 5))
plt.scatter(ns, counts, s=20, color="#1f3a93", label="computed")
plt.plot(ns, predicted, "--", color="#c0392b", label=r"$24\,\sigma_{\mathrm{odd}}(n)$")
plt.xlabel(r"$n$")
plt.ylabel(r"number of Hurwitz integers of norm $n$")
plt.title("Count of Hurwitz integers of each norm")
plt.legend()
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig("figures/fig_counts.png", dpi=150)
plt.close()
print("wrote figures/fig_counts.png")
