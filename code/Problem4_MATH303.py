"""
MATH 303 - Linear and Nonlinear Programming
Problem 4

    Max  f = x1 + 2 x2 + 2 x3
    s.t. 5x1 + 2x2 + 3x3 <= 15
          x1 + 4x2 + 2x3 <= 12
         2x1       +  x3 <= 8
         x1, x2, x3 >= 0

linprog only minimizes, so we solve  Min f = -(x1 + 2 x2 + 2 x3).
"""
from scipy.optimize import linprog

c = [-1, -2, -2]                    # Min f = -(x1 + 2x2 + 2x3)
A_ub = [[5, 2, 3],
        [1, 4, 2],
        [2, 0, 1]]
b_ub = [15, 12, 8]
bounds = [(0, None)] * 3

res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")

print("Status :", res.message)
for i, v in enumerate(res.x, start=1):
    print(f"x{i} = {v:.4f}")
print(f"Max f = {-res.fun:.4f}")
print("Slacks (x4, x5, x6):", res.slack)
