import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from collections import Counter
from figure_common import norm, sub, enumerate_hurwitz_by_norm, make_prime_sieve, prime_points_up_to

M = 150
by_norm = enumerate_hurwitz_by_norm(M)
sieve = make_prime_sieve(4 * M + 10)
pp = prime_points_up_to(by_norm, M, sieve)

def minimal_smaller(alpha):
    for p in sorted(pp):
        for pi in pp[p]:
            if sieve[norm(sub(alpha, pi))]:
                return p
    return None

tally = Counter()
for n in range(2, M + 1):
    for alpha in by_norm[n]:
        tally[minimal_smaller(alpha)] += 1

labels = sorted(tally)
counts = [tally[p] for p in labels]

plt.figure(figsize=(8, 5))
plt.bar([str(p) for p in labels], counts, color=["#1f3a93", "#16a085", "#c0392b"])
for i, c in enumerate(counts):
    plt.text(i, c + 4000, str(c), ha="center", fontsize=9)
plt.xlabel("minimal smaller prime norm")
plt.ylabel("number of targets")
plt.title("Minimal smaller prime norm needed, 2 <= N <= 150")
plt.grid(alpha=0.25, axis="y")
plt.tight_layout()
plt.savefig("figures/fig_smaller_prime_hist.png", dpi=150)
plt.close()
print("wrote figures/fig_smaller_prime_hist.png")
print(tally)
