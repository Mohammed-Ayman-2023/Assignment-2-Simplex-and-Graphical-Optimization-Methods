"""
MATH 303 - Linear and Nonlinear Programming
Problem 2

    Max  f = x - 8y
    s.t. 3x + 2y >= 6
          x -  y <= 6
         9x + 7y <= 108
         3x + 7y <= 70
         2x - 5y >= -35
         x, y >= 0

Converted for linprog (Min, all constraints as <=):
    Min f = -(x - 8y) = -x + 8y
    -3x - 2y <= -6
     -2x + 5y <= 35
"""
from scipy.optimize import linprog

c = [-1, 8]                         # Min f = -x + 8y
A_ub = [[-3, -2],                   # 3x + 2y >= 6
        [1, -1],
        [9, 7],
        [3, 7],
        [-2, 5]]                    # 2x - 5y >= -35
b_ub = [-6, 6, 108, 70, 35]
bounds = [(0, None), (0, None)]

res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")

print("Status :", res.message)
print(f"x = {res.x[0]:.4f}")
print(f"y = {res.x[1]:.4f}")
print(f"Max f = {-res.fun:.4f}")
