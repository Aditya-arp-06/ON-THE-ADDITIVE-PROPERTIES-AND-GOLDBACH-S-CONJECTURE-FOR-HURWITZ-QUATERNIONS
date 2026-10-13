import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from figure_common import norm, sub, enumerate_hurwitz_by_norm, make_prime_sieve, prime_points_up_to
from sympy import isprime

def d_count(alpha, n, p1, p2, pp, sieve):
    c2 = 0
    for pi in pp.get(p1, []):
        if sieve[norm(sub(alpha, pi))]:
            c2 += 1
    return c2

M = 40
by_norm = enumerate_hurwitz_by_norm(M)
sieve = make_prime_sieve(4 * M + 10)
pp = prime_points_up_to(by_norm, M, sieve)

targets = []
for n in [9, 10, 18, 36]:
    targets.append((by_norm[n][0], n))

rho2_vals, counts = [], []
for alpha, n in targets:
    for p1 in [2, 3, 5, 7]:
        if p1 not in pp:
            continue
        for p2 in [2, 3, 5, 7, 11]:
            if p2 not in pp:
                continue
            c = (n + p1 - p2) / 2
            rho2 = p1 - (c * c) / n
            rho2_vals.append(rho2)
            counts.append(d_count(alpha, n, p1, p2, pp, sieve))

plt.figure(figsize=(8, 5))
plt.scatter(rho2_vals, counts, s=20, color="#1f3a93")
plt.axvline(0, color="#c0392b", linestyle="--", label=r"$\rho^2=0$")
plt.xlabel(r"$\rho^2=p_1-c^2/N(\alpha)$")
plt.ylabel(r"$\#\mathrm{D}(\alpha;p_1,p_2)$")
plt.title("Hyperplane reduction: no decomposition once the sphere radius is imaginary")
plt.legend()
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig("figures/fig_sphere_radius.png", dpi=150)
plt.close()
print("wrote figures/fig_sphere_radius.png")

# ---------------------------------------------------------------------
# Terminal output:  python fig2.py
# ---------------------------------------------------------------------
# wrote figures/fig_sphere_radius.png
