# Assignment 2: Simplex and Graphical Optimization Methods

MATH 303: Linear and Nonlinear Programming, Zewail City of Science and Technology.

Four linear programming problems, each solved with the graphical method, the simplex method (Big-M for artificial variables), and a Python LP solver.

## Contents

| Path | Description |
|---|---|
| `report/MATH303_Assignment_Solutions.pdf` | Full answer document: formulations, simplex tableaux, graphs, solver output |
| `report/MATH303_Assignment_Solutions.tex` | LaTeX source of the report (TikZ / pgfplots graphs) |
| `code/Problem1_MATH303.py` | PCB production problem |
| `code/Problem2_MATH303.py` | Problem 2 |
| `code/Problem3_MATH303.py` | Problem 3, minimization and part (d) maximization |
| `code/Problem4_MATH303.py` | Three-variable problem |

## Results

| Problem | Optimal solution | Optimal value |
|---|---|---|
| 1 | x1 = 62.5, x2 = 31.25 | max profit = 1093.75 |
| 2 | x = 6, y = 0 | max f = 6 |
| 3 | x1 = 0, x2 = 5 | min f = 20 |
| 3 (d) | x1 = 4, x2 = 4 | max f = 24 |
| 4 | x1 = 0, x2 = 3/4, x3 = 9/2 | max f = 10.5 |

## Running the solvers

```bash
pip install scipy
python code/Problem1_MATH303.py
```

## Building the report

```bash
cd report
pdflatex MATH303_Assignment_Solutions.tex
pdflatex MATH303_Assignment_Solutions.tex
```
