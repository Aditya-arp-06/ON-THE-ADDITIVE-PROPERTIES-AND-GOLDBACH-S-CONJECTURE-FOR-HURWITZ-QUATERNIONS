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

# ---------------------------------------------------------------------
# Terminal output:  python inspect_stats.py
# ---------------------------------------------------------------------
# n #alpha min R max R mean
#  2    24     8     8      8.0
#  3    96    68    68     68.0
#  4    24    70    70     70.0
#  5   144   135   135    135.0
#  6    96   161   161    161.0
#  7   192   195   195    195.0
#  8    24   271   271    271.0
#  9   312   197   230    199.5
# 10   144   241   241    241.0
# 11   288   279   279    279.0
# 12    96   384   384    384.0
# 13   336   361   373    366.1
# 14   192   495   495    495.0
# 15   576   382   382    382.0
# 16    24   466   466    466.0
# 17   432   479   484    482.3
# 18   312   718  1086    746.3
# 19   480   570   605    584.0
# 20   144   861   861    861.0
# 21   768   630   640    632.5
# 22   288   830   830    830.0
# 23   576   743   743    743.0
# 24    96  1185  1185   1185.0
# 25   744   696   850    714.1
# 26   336  1048  1065   1057.7
# 27   960   757  1189    800.5
# 28   192  1000  1000   1000.0
# 29   720   920   931    922.2
# 30   576  1442  1442   1442.0
# 31   768  1034  1046   1043.0
# 32    24  1596  1596   1596.0
# 33  1152  1134  1164   1142.8
# 34   432  1486  1503   1491.7
# 35  1152  1079  1094   1086.5
# 36   312  1649  2602   1722.3
# 37   912  1228  1247   1236.7
# 38   480  1812  1824   1816.8
# 39  1344  1338  1360   1341.1
# 40   144  1869  1869   1869.0
