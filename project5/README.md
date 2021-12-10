# Knapsack Approximation Algorithm

Empirical studies on a Knapsack approximation algorithm: In class we discussed a **greedy 2-approximation algorithm** for the Knapsack problem; this algorithm performed two independent greedy searches (the firrst ordered items by value, the second ordered items by value/weight) and returned the best subset found.

## Deliverables

#### Deliverable 1

Source code. Discuss how you would verify that this algorithm is implemented correctly. Since it is approximate, verifiation is not as simple as checking your answers against another algorithm!

#### Deliverable 2

A scatter plot with problem instance on the horizontal axis and approximation ratio on the vertical axis. This may look very messy, but it should be clear that no instance has an approximation ratio greater than 2.

#### Deliverable 3

Report the average approximation ratio of this greedy algorithm across all of your trials from Deliverable 2.

## Files

| Filename | Description |
|--- |--- |
| [approximate.py](approximate.py) | Main program that calculate approximation ratio between the best result of two greedy Knapsack algorithm and an optimal solution (buttom up dynamic programming Knapsack algorithm). |
| [buknapsack.py](buknapsack.py) | The Bottom Up Knapsask Algorithm. Save version of [buknapsack.py](../project3/buknapsack.py) from Project 3. |
| [greedy.py](greedy.py) | A updated version of [greedy](../project1/greedy.py) Knapsack algorithm from Project 1. |
| [valueweight.py](valueweight.py) | Greedy Knapsack algorithms, that utilize value/weight as the sorting mechanism. |

