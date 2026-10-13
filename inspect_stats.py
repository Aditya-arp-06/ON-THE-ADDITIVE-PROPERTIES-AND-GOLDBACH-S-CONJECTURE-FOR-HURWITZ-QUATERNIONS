from collections import defaultdict
from hurwitz_engine import norm, sub, enumerate_hurwitz_by_norm, make_prime_sieve

def r_of(alpha, n, prime_points, sieve):
    cnt = 0
    for p, pts in prime_points.items():
        if p > n:
            continue
        for pi in pts:
            if sieve[norm(sub(alpha, pi))]:
                cnt += 1
    return cnt

if __name__ == "__main__":
    M = 40
    by_norm = enumerate_hurwitz_by_norm(M)
    sieve = make_prime_sieve(4 * M + 10)
    prime_points = {p: pts for p, pts in by_norm.items() if 2 <= p <= M and sieve[p]}
    print("n #alpha min R max R mean")
    for n in range(2, M + 1):
        vals = [r_of(alpha, n, prime_points, sieve) for alpha in by_norm[n]]
        mean = sum(vals) / len(vals)
        print(f"{n:>2} {len(vals):>5} {min(vals):>5} {max(vals):>5} {mean:>8.1f}")
