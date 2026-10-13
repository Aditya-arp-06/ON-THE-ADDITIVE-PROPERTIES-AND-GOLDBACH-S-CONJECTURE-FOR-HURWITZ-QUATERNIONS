from collections import defaultdict

def is_hurwitz(q):
    A, B, C, D = q
    return len({A & 1, B & 1, C & 1, D & 1}) == 1

def norm(q):
    A, B, C, D = q
    return (A * A + B * B + C * C + D * D) // 4

def trace(q):
    return q[0]

def conj(q):
    A, B, C, D = q
    return (A, -B, -C, -D)

def add(q1, q2):
    return (q1[0] + q2[0], q1[1] + q2[1], q1[2] + q2[2], q1[3] + q2[3])

def sub(q1, q2):
    return (q1[0] - q2[0], q1[1] - q2[1], q1[2] - q2[2], q1[3] - q2[3])

def hamilton(q1, q2):
    A1, B1, C1, D1 = q1
    A2, B2, C2, D2 = q2
    A = (A1 * A2 - B1 * B2 - C1 * C2 - D1 * D2) // 2
    B = (A1 * B2 + B1 * A2 + C1 * D2 - D1 * C2) // 2
    C = (A1 * C2 - B1 * D2 + C1 * A2 + D1 * B2) // 2
    D = (A1 * D2 + B1 * C2 - C1 * B2 + D1 * A2) // 2
    return (A, B, C, D)

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

# ---------------------------------------------------------------------
# Terminal output:  none - library module, imported by the other scripts
# ---------------------------------------------------------------------
