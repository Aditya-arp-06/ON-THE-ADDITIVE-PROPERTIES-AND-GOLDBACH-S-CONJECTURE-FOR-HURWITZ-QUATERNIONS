from sympy import isprime
from hurwitz_engine import norm, trace, is_hurwitz

def three_squares(N):
    sols = []
    r = int(N ** 0.5) + 1
    for x in range(-r, r + 1):
        x2 = x * x
        if x2 > N:
            continue
        for y in range(-r, r + 1):
            y2 = x2 + y * y
            if y2 > N:
                continue
            for z in range(-r, r + 1):
                if y2 + z * z == N:
                    sols.append((x, y, z))
    return sols

def real_axis_prime(n):
    if n % 2 == 1:
        p = 3
        while True:
            N = 4 * p - n * n
            if N > 0 and three_squares(N):
                return p, three_squares(N)[0]
            p += 2
            while not isprime(p):
                p += 2
    else:
        m = n // 2
        p = 2
        while True:
            if p > m * m and isprime(p):
                N = p - m * m
                s = three_squares(N)
                if s:
                    return p, s[0]
            p += 1

def build_pi(n, p, triple):
    if n % 2 == 1:
        b, c, d = triple
        return (n, b, c, d)
    else:
        b, c, d = triple
        return (2 * (n // 2), 2 * b, 2 * c, 2 * d)

def verify_real_axis(nmax):
    for n in range(2, nmax + 1):
        p, triple = real_axis_prime(n)
        pi = build_pi(n, p, triple)
        assert is_hurwitz(pi), f"not Hurwitz at n={n}"
        assert norm(pi) == p, f"norm mismatch at n={n}"
        assert trace(pi) == n, f"trace mismatch at n={n}"
    print(f"real axis Goldbach verified for every n in 2..{nmax}")

def verify_twin(limit):
    pairs = []
    c, d = 0, 0
    while len(pairs) < limit:
        if isprime(c * c + d * d + 1):
            pi = (0, -2, 2 * c, 2 * d)
            twin = (2, 0, 2 * c, 2 * d)
            assert norm(pi) == norm(twin) == c * c + d * d + 1
            assert is_hurwitz(pi) and is_hurwitz(twin)
            pairs.append((c, d))
        d += 1
        if d > 20:
            d = 0
            c += 1
    print(f"twin family verified for first {limit} pairs: {pairs}")

if __name__ == "__main__":
    verify_real_axis(120)
    verify_twin(8)

# ---------------------------------------------------------------------
# Terminal output:  python verify_new_theorems.py
# ---------------------------------------------------------------------
# real axis Goldbach verified for every n in 2..120
# twin family verified for first 8 pairs: [(0, 1), (0, 2), (0, 4), (0, 6), (0, 10), (0, 14), (0, 16), (0, 20)]
