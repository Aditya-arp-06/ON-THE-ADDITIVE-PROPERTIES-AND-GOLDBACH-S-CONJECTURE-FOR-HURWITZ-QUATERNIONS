import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from figure_common import enumerate_hurwitz_by_norm, make_prime_sieve

M = 40
by_norm = enumerate_hurwitz_by_norm(M)
sieve = make_prime_sieve(M + 1)
primes = [p for p in range(2, M + 1) if sieve[p]]
counts = [len(by_norm[p]) for p in primes]
predicted = [24 if p == 2 else 24 * (p + 1) for p in primes]

plt.figure(figsize=(8, 5))
plt.scatter(primes, counts, s=20, color="#1f3a93", label="computed")
plt.plot(primes, predicted, "--", color="#c0392b", label=r"$24(p+1)$")
plt.xlabel(r"$p$")
plt.ylabel(r"number of Hurwitz primes of norm $p$")
plt.title("Hurwitz primes of norm p against 24(p+1)")
plt.legend()
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig("figures/fig_primecount.png", dpi=150)
plt.close()
print("wrote figures/fig_primecount.png")

# ---------------------------------------------------------------------
# Terminal output:  python fig6.py
# ---------------------------------------------------------------------
# wrote figures/fig_primecount.png
