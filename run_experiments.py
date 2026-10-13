import json
from collections import defaultdict
from sympy import isprime
from hurwitz_engine import norm, sub, enumerate_hurwitz_by_norm, make_prime_sieve

def decompose_all(M):
    by_norm = enumerate_hurwitz_by_norm(M)
    sieve = make_prime_sieve(4 * M + 10)
    prime_points = {p: pts for p, pts in by_norm.items() if 2 <= p <= M and sieve[p]}
    R = {}
    total = 0
    for n in range(2, M + 1):
        for alpha in by_norm[n]:
            cnt = 0
            for p, pts in prime_points.items():
                if p > n:
                    continue
                for pi in pts:
                    m = norm(sub(alpha, pi))
                    if m < len(sieve) and sieve[m]:
                        cnt += 1
            R[alpha] = cnt
            total += cnt
    return by_norm, R, total

if __name__ == "__main__":
    M = 40
    by_norm, R, total = decompose_all(M)
    n_targets = sum(len(by_norm[n]) for n in range(2, M + 1))
    print("targets with 2 <= N <= 40:", n_targets)
    print("ordered decompositions found:", total)
    print("minimum of R:", min(R.values()))
    print("maximum of R:", max(R.values()))

# ---------------------------------------------------------------------
# Terminal output:  python run_experiments.py
# ---------------------------------------------------------------------
# targets with 2 <= N <= 40: 15912
# ordered decompositions found: 14865240
# minimum of R: 8
# maximum of R: 2602
