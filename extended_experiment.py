from collections import Counter
from hurwitz_engine import norm, sub, enumerate_hurwitz_by_norm, make_prime_sieve

def minimal_smaller_prime(alpha, prime_points, sieve):
    for p in sorted(prime_points):
        for pi in prime_points[p]:
            if sieve[norm(sub(alpha, pi))]:
                return p
    return None

if __name__ == "__main__":
    M = 150
    by_norm = enumerate_hurwitz_by_norm(M)
    sieve = make_prime_sieve(4 * M + 10)
    prime_points = {p: pts for p, pts in by_norm.items() if 2 <= p <= M and sieve[p]}
    tally = Counter()
    for n in range(2, M + 1):
        for alpha in by_norm[n]:
            p = minimal_smaller_prime(alpha, prime_points, sieve)
            assert p is not None and p <= 5, f"smaller prime > 5 at norm {n}"
            tally[p] += 1
    print("minimal smaller prime norm needed, 2 <= N <= 150:")
    for p in sorted(tally):
        print(f"  {p}: {tally[p]} targets")
    print("total:", sum(tally.values()))

# ---------------------------------------------------------------------
# Terminal output:  python extended_experiment.py
# ---------------------------------------------------------------------
# minimal smaller prime norm needed, 2 <= N <= 150:
#   2: 166800 targets
#   3: 56136 targets
#   5: 624 targets
# total: 223560
