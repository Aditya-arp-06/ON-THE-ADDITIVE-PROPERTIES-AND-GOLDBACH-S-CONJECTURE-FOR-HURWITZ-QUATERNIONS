import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from figure_common import norm, sub, enumerate_hurwitz_by_norm, make_prime_sieve, prime_points_up_to

M = 40
by_norm = enumerate_hurwitz_by_norm(M)
sieve = make_prime_sieve(4 * M + 10)
pp = prime_points_up_to(by_norm, M, sieve)

odd_counts = []
for n in range(2, M + 1):
    odd = 0
    for alpha in by_norm[n]:
        d = 0
        for p, pts in pp.items():
            if p > n:
                continue
            for pi in pts:
                m = norm(sub(alpha, pi))
                if m <= n and sieve[m]:
                    d += 1
        if d % 2 == 1:
            odd += 1
    odd_counts.append((n, odd))

ns = [n for n, _ in odd_counts]
odds = [o for n, o in odd_counts]

plt.figure(figsize=(8, 5))
plt.bar(ns, odds, color="#1f3a93", alpha=0.8)
plt.xlabel(r"$N(\alpha)$")
plt.ylabel(r"number of $\alpha$ with odd $D(\alpha)$")
plt.title("Symmetric count is odd exactly when $\\alpha/2$ is a Hurwitz prime (Theorem 8.9)")
plt.grid(alpha=0.25, axis="y")
plt.tight_layout()
plt.savefig("figures/fig_D_parity.png", dpi=150)
plt.close()
print("wrote figures/fig_D_parity.png")
print("norms with odd-D targets:", [(n, o) for n, o in odd_counts if o > 0])
