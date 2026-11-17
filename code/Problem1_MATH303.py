"""
MATH 303 - Linear and Nonlinear Programming
Problem 1: PCB production (boards A and B)

    Max  f = 10 x1 + 15 x2            (x1 = units of A, x2 = units of B)
    s.t. 16 x1 + 10 x2 <= 1500        component placement
         10 x1 + 12 x2 <= 1000        soldering
          4 x1 +  8 x2 <=  500        inspection
         x1, x2 >= 0

linprog only minimizes, so we solve  Min f = -(10 x1 + 15 x2).
"""
from scipy.optimize import linprog

c = [-10, -15]                      # Min f = -(10 x1 + 15 x2)
A_ub = [[16, 10],
        [10, 12],
        [4, 8]]
b_ub = [1500, 1000, 500]
bounds = [(0, None), (0, None)]

res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")

print("Status :", res.message)
print(f"x1 (A) = {res.x[0]:.4f}")
print(f"x2 (B) = {res.x[1]:.4f}")
print(f"Max profit f = {-res.fun:.4f}")
print("Slacks (placement, soldering, inspection):", res.slack)
