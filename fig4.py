import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from figure_common import norm, sub, enumerate_hurwitz_by_norm, make_prime_sieve, prime_points_up_to

M = 40
by_norm = enumerate_hurwitz_by_norm(M)
sieve = make_prime_sieve(4 * M + 10)
pp = prime_points_up_to(by_norm, M, sieve)

def minimal_smaller(alpha, n):
    for p in sorted(pp):
        if p > n:
            break
        for pi in pp[p]:
            if sieve[norm(sub(alpha, pi))]:
                return p
    return None

ns, qmax = [], []
for n in range(2, M + 1):
    need = max(minimal_smaller(alpha, n) for alpha in by_norm[n])
    ns.append(n)
    qmax.append(need)

plt.figure(figsize=(8, 5))
plt.scatter(ns, qmax, color="#1f3a93", s=40)
plt.xlabel(r"$N(\alpha)$")
plt.ylabel(r"largest smaller prime norm needed")
plt.title("Odd norms use 2; even norms need 3; multiples of 18 need 5 (Theorem 11.5)")
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig("figures/fig_parity.png", dpi=150)
plt.close()
print("wrote figures/fig_parity.png")
