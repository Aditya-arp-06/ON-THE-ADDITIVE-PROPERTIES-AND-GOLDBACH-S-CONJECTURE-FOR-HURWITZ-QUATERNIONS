# On the Additive Properties and Goldbach's Conjecture for Hurwitz Quaternions

This repository contains the complete source code for the research project
*On the Additive Properties and Goldbach's Conjecture for Hurwitz Quaternions*.

## The research project

Quaternions are four-dimensional numbers $\alpha = a + bi + cj + dk$ whose imaginary
units satisfy $i^2 = j^2 = k^2 = ijk = -1$. The reduced norm
$N(\alpha) = a^2 + b^2 + c^2 + d^2$ measures squared Euclidean distance in
$\mathbb{R}^4$, and in the Hurwitz integers $\mathcal{O}$ an element is prime exactly
when its norm is an ordinary rational prime.

In 2016 Oliver Knill formulated an experimental version of the **Quaternion Goldbach
Conjecture** on coordinate-restricted quaternions. This project investigates the full,
unrestricted problem: whether every $\alpha \in \mathcal{O}$ with $N(\alpha) \ge 2$
decomposes as a sum of two Hurwitz primes, $\alpha = \pi_1 + \pi_2$.

### Main results

- **Hyperplane Reduction Theorem.** Fixing the prime norms $(p_1, p_2)$ restricts the
  candidate summands to an affine 2-sphere of radius
  $\rho = \sqrt{p_1 - c^2/N(\alpha)}$.
- **Norm Interval Theorem** (unconditional), with sharp integer floor bounds:
  $(\sqrt{p_1} - \sqrt{p_2})^2 \le N(\alpha) \le (\sqrt{p_1} + \sqrt{p_2})^2$.
- **Deterministic packing bound.** There are at most $24\rho^2 + 2$ valid prime
  decompositions.
- **Exact local obstructions.** Even norms exceeding eight exclude norm-two primes, and
  multiples of eighteen require prime norms of at least five — paralleling the classical
  parity phenomena over the integers.
- **Two unconditional existence results.** (1) Every integer $n \ge 2$ on the real axis
  decomposes as $n = \pi + \bar{\pi}$, via Legendre's three-square theorem and
  Dirichlet's theorem on arithmetic progressions. (2) There are infinitely many twin
  Hurwitz primes differing by $1+i$, via Iwaniec's theorem (and for all twenty-four
  shifts of norm two, via Linnik and Iwaniec).

### Computational verification

Exact integer algorithms — no floating-point number enters any count — confirmed the
conjecture for all **39,476,352 targets up to norm 2,000**, and revealed a linear
*Quaternion Goldbach Comet*, with the representation count growing consistently with a
Hardy–Littlewood type asymptotic.

While the general existence conjecture remains open, these results establish that
additive prime questions in non-commutative lattices can be approached directly through
quadratic geometry. The primary open problems are evaluating the singular series product
of local densities in closed form, and extending the geometric reduction to other
maximal quaternion orders.

### Prior presentation

Earlier stages of this research were selected for an Oral Presentation Assessment at the
S.-T. Yau High School Science Award Asia (YHSA) and presented at the 4th International
Mathematics and Statistics Student Research Symposium (IMSSRS).

## The code

All arithmetic is exact integer arithmetic on **doubled coordinates**: a Hurwitz integer
$a + bi + cj + dk$ is stored as the integer quadruple $(2a, 2b, 2c, 2d)$, so the norm
$(A^2+B^2+C^2+D^2)/4$ and the trace $A$ are exact integers.

| Script | Produces |
| --- | --- |
| `hurwitz_engine.py` | Doubled-coordinate arithmetic, norm, trace, conjugation, Hamilton product, prime sieve, enumeration of Hurwitz integers by norm |
| `run_experiments.py` | The exhaustive sweep: 15,912 targets of norm 2–40 and 14,865,240 ordered decompositions |
| `extended_experiment.py` | The bounded smaller-prime census for norms 2–150 |
| `verify_new_theorems.py` | Verification of the real-axis and twin-prime theorems |
| `verify_added_theorems.py` | Verification that $R(\alpha)=8$ on the norm-2 shell, and the norm-18 census |
| `verify_examples.py` | Verification of all explicit decompositions |
| `verify_n450.py` | The $p^\star = 7$ example at norm 450 |
| `inspect_stats.py` | Representation-count statistics for every norm from 2 to 40 |
| `figure_common.py` | Shared helpers imported by the figure scripts |
| `figure1_standalone.py` | Figure 1 — the trace band |
| `figure11_standalone.py` | Figure 11 — the distribution of $R(\alpha)$ |
| `fig2.py` | Figure 2 — the hyperplane reduction |
| `fig3.py` | Figure 3 — parity of the symmetric count |
| `fig4.py` | Figure 4 — largest smaller prime norm needed |
| `fig5.py` | Figure 5 — count of Hurwitz integers of each norm |
| `fig6.py` | Figure 6 — count of Hurwitz primes of each norm |
| `fig7.py` | Figure 7 — the Goldbach comet |
| `fig8.py` | Figure 8 — envelope of the representation count |
| `fig9.py` | Figure 9 — logarithmic growth |
| `fig10.py` | Figure 10 — lower envelope fit |
| `fig12.py` | Figure 12 — minimal smaller prime census |
| `fig13.py` | Figure 13 — real-axis smallest prime |
| `fig14.py` | Figure 14 — self-conjugate count |
| `fig15.py` | Figure 15 — twin prime growth |

### Requirements

```
pip install numpy matplotlib sympy
```

### Run order

```
python run_experiments.py
python extended_experiment.py
python verify_new_theorems.py
python verify_added_theorems.py
python verify_examples.py
python verify_n450.py
python inspect_stats.py
python figure1_standalone.py
python figure11_standalone.py
```

The remaining `fig*.py` scripts regenerate the corresponding figures.
