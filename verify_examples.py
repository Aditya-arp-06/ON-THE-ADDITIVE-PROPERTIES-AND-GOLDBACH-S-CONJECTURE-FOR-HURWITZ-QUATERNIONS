from hurwitz_engine import norm, add, is_hurwitz
from sympy import isprime

def q(a, b, c, d):
    return (2 * a, 2 * b, 2 * c, 2 * d)

def check(target, s1, s2, p1, p2):
    assert add(s1, s2) == target, f"sum mismatch for {target}"
    assert norm(s1) == p1 and isprime(p1), f"summand 1 not prime norm {p1}"
    assert norm(s2) == p2 and isprime(p2), f"summand 2 not prime norm {p2}"
    assert is_hurwitz(s1) and is_hurwitz(s2)

examples = [
    (q(1, 1, 0, 0), q(0, 1, 1, 0), q(1, 0, -1, 0), 2, 2),
    (q(1, 1, 1, 0), q(0, 0, 1, 1), q(1, 1, 0, -1), 2, 3),
    (q(1, 2, 0, 0), q(0, 1, 1, 0), q(1, 1, -1, 0), 2, 3),
    (q(1, 1, 1, 1), q(1, 1, 0, 0), q(0, 0, 1, 1), 2, 2),
    (q(2, 0, 0, 0), q(1, 1, 0, 0), q(1, -1, 0, 0), 2, 2),
    (q(2, 2, 0, 0), q(1, 1, 0, 0), q(1, 1, 0, 0), 2, 2),
    (q(3, 0, 0, 0), q(1, 1, 0, 0), q(2, -1, 0, 0), 2, 5),
    (q(3, 3, 0, 0), q(2, 1, 0, 0), q(1, 2, 0, 0), 5, 5),
    (q(1, 1, 2, 0), q(0, 1, 1, 0), q(1, 0, 1, 0), 2, 2),
    (q(2, 2, 1, 0), q(1, 1, 0, 0), q(1, 1, 1, 0), 2, 3),
    (q(3, 1, 0, 0), (3, 1, 1, -1), (3, 1, -1, 1), 3, 3),
    (q(4, 0, 0, 0), (3, 1, 1, 1), (5, -1, -1, -1), 3, 7),
    (q(6, 0, 0, 0), q(2, 1, 0, 0), q(4, -1, 0, 0), 5, 17),
]

if __name__ == "__main__":
    for target, s1, s2, p1, p2 in examples:
        check(target, s1, s2, p1, p2)
    print(f"all {len(examples)} explicit decompositions verified")

# ---------------------------------------------------------------------
# Terminal output:  python verify_examples.py
# ---------------------------------------------------------------------
# all 13 explicit decompositions verified
