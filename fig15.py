import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sympy import isprime

def twin_count(B):
    cnt = 0
    for c in range(-B, B + 1):
        for d in range(-B, B + 1):
            if isprime(c * c + d * d + 1):
                cnt += 1
    return cnt

Bs = list(range(1, 31))
counts = [twin_count(B) for B in Bs]
Bs = np.array(Bs)
counts = np.array(counts)
ref = Bs * Bs / np.log(Bs + 1)

plt.figure(figsize=(8, 5))
plt.plot(Bs, counts, "o-", color="#1f3a93", label=r"computed count")
plt.plot(Bs, ref, "--", color="#c0392b", label=r"$B^2/\log B$")
plt.xlabel(r"$B$")
plt.ylabel(r"number of $(c,d)$ with $c^2+d^2+1$ prime")
plt.title("Twin Hurwitz primes for the shift 1+i")
plt.legend()
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig("figures/fig_twin_growth.png", dpi=150)
plt.close()
print("wrote figures/fig_twin_growth.png")

# ---------------------------------------------------------------------
# Terminal output:  python fig15.py
# ---------------------------------------------------------------------
# wrote figures/fig_twin_growth.png
