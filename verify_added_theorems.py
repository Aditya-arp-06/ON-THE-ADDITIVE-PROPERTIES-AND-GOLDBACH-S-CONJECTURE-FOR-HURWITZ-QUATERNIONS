from hurwitz_engine import norm, sub, enumerate_hurwitz_by_norm, make_prime_sieve

def sigma_odd(n):
    return sum(d for d in range(1, n + 1) if n % d == 0 and d % 2 == 1)

def verify_norm_two_exact():
    by_norm = enumerate_hurwitz_by_norm(2)
    sieve = make_prime_sieve(40)
    for alpha in by_norm[2]:
        cnt = 0
        for pi in by_norm[2]:
            if sieve[norm(sub(alpha, pi))]:
                cnt += 1
        assert cnt == 8, f"R({alpha}) != 8"
    print("Theorem 9.6 verified: R(alpha) = 8 on all 24 targets of norm 2")

def verify_needfive_census():
    by_norm = enumerate_hurwitz_by_norm(150)
    sieve = make_prime_sieve(4 * 150 + 10)
    prime3 = by_norm[3]
    for m in [1, 2, 3, 4, 5, 6, 7, 8]:
        expected = 24 * sigma_odd(2 * m)
        blocked = 0
        for beta in by_norm[2 * m]:
            alpha = (3 * beta[0], 3 * beta[1], 3 * beta[2], 3 * beta[3])
            assert norm(alpha) == 18 * m
            has_three = any(sieve[norm(sub(alpha, pi))] for pi in prime3)
            assert not has_three, "norm-3 prime is a summand of a 3|alpha target"
            blocked += 1
        assert blocked == expected, f"census mismatch at n=18m, m={m}: {blocked} != {expected}"
    print("Theorem 11.5 census verified: 24 sigma_odd(2m) at every norm 18m, m=1..8")

if __name__ == "__main__":
    verify_norm_two_exact()
    verify_needfive_census()
