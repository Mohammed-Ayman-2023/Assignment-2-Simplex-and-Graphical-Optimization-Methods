"""
MATH 303 - Linear and Nonlinear Programming
Problem 3

    (a-c) Min f = 2 x1 + 4 x2
    (d)   Max f = 2 x1 + 4 x2   ->  Min f = -(2 x1 + 4 x2)
    s.t.   x1 +   x2 <= 8
          6x1 + 4 x2 >= 12
           x1 + 4 x2  = 20
          x1, x2 >= 0
"""
from scipy.optimize import linprog

A_ub = [[1, 1],
        [-6, -4]]                   # 6x1 + 4x2 >= 12
b_ub = [8, -12]
A_eq = [[1, 4]]
b_eq = [20]
bounds = [(0, None), (0, None)]


def solve(c, label, sign):
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                  bounds=bounds, method="highs")
    print(label)
    print("  Status :", res.message)
    print(f"  x1 = {res.x[0]:.4f}")
    print(f"  x2 = {res.x[1]:.4f}")
    print(f"  f  = {sign * res.fun:.4f}\n")


solve([2, 4], "Minimize f = 2 x1 + 4 x2", +1)
solve([-2, -4], "(d) Maximize f = 2 x1 + 4 x2", -1)
