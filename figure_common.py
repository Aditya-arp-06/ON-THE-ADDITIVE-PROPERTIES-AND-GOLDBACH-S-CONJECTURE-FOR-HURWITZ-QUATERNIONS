from collections import defaultdict, Counter

def is_hurwitz(q):
    A, B, C, D = q
    return len({A & 1, B & 1, C & 1, D & 1}) == 1

def norm(q):
    A, B, C, D = q
    return (A * A + B * B + C * C + D * D) // 4

def trace(q):
    return q[0]

def sub(q1, q2):
    return (q1[0] - q2[0], q1[1] - q2[1], q1[2] - q2[2], q1[3] - q2[3])

def make_prime_sieve(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return sieve

def enumerate_hurwitz_by_norm(nmax):
    by_norm = defaultdict(list)
    R = int((4 * nmax) ** 0.5) + 1
    for A in range(-R, R + 1):
        a2 = A * A
        if a2 > 4 * nmax:
            continue
        for B in range(-R, R + 1):
            b2 = a2 + B * B
            if b2 > 4 * nmax:
                continue
            for C in range(-R, R + 1):
                c2 = b2 + C * C
                if c2 > 4 * nmax:
                    continue
                for D in range(-R, R + 1):
                    s = c2 + D * D
                    if s > 4 * nmax or s % 4 != 0:
                        continue
                    q = (A, B, C, D)
                    if is_hurwitz(q):
                        by_norm[s // 4].append(q)
    return by_norm

def sigma_odd(n):
    return sum(d for d in range(1, n + 1) if n % d == 0 and d % 2 == 1)

def prime_points_up_to(by_norm, M, sieve):
    return {p: pts for p, pts in by_norm.items() if 2 <= p <= M and sieve[p]}

def r_of(alpha, n, prime_points, sieve):
    cnt = 0
    for p, pts in prime_points.items():
        if p > n:
            continue
        for pi in pts:
            if sieve[norm(sub(alpha, pi))]:
                cnt += 1
    return cnt

def r_all(M):
    by_norm = enumerate_hurwitz_by_norm(M)
    sieve = make_prime_sieve(4 * M + 10)
    pp = prime_points_up_to(by_norm, M, sieve)
    R = {}
    for n in range(2, M + 1):
        for alpha in by_norm[n]:
            R[alpha] = r_of(alpha, n, pp, sieve)
    return by_norm, R

# ---------------------------------------------------------------------
# Terminal output:  none - library module, imported by the other scripts
# ---------------------------------------------------------------------
