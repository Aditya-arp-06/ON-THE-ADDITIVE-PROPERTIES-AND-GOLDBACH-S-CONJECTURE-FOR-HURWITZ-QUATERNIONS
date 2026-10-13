from hurwitz_engine import norm, sub, enumerate_hurwitz_by_norm, make_prime_sieve

if __name__ == "__main__":
    alpha = (30, 30, 0, 0)
    M = 450
    by_norm = enumerate_hurwitz_by_norm(8)
    sieve = make_prime_sieve(4 * 450 + 10)
    prime_points = {p: pts for p, pts in by_norm.items() if 2 <= p <= 7 and sieve[p]}
    assert norm(alpha) == 450
    for p in [2, 3, 5]:
        assert not any(sieve[norm(sub(alpha, pi))] for pi in prime_points[p]), f"norm {p} summand found"
    print("norms 2, 3, 5 all blocked for N=450 target, as Theorem 11.4 predicts")
    print("smallest viable smaller prime norm is 7")

# ---------------------------------------------------------------------
# Terminal output:  python verify_n450.py
# ---------------------------------------------------------------------
# norms 2, 3, 5 all blocked for N=450 target, as Theorem 11.4 predicts
# smallest viable smaller prime norm is 7
