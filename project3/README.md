# Dynamic Programming and Knapsack

This project is to implement two version of a DP algorithm for the Knapsak problem: a **bottom-up version** that computes the solutions to all subproblems (without repeating any solutions), and a **top-down version** that uses memoization (the book calls this the “memory functions” approach) to ensure that we solve only the subproblems that need to be solved. 

This project explores this speedup, and looks for potential tradeoffs in this space.

## Deliverables

#### Deliverable 1

Your implementation’s code and your verification of correctness.

#### Deliverable 2

Plots showing the time performance of your algorithm as a function of n and W for each algorithm, and discussion about the reasons for any performance differences between the two algorithms.

#### Deliverable 3

Plots showing the time performance of your algorithm as a function of n and W for each algorithm on special inputs, and discussion about the reasons for any performance differences between the two algorithms.

#### Deliverable 4

 Illustrate that this is a pseudopolynomial-time algorithm.

## Files

| Filename | Description |
|--- |--- |
| [buknapsack.py](buknapsack.py) | The Bottom Up Knapsask Algorithm. |
| [mfknapsack.py](mfknapsack.py) | The Top Down, aka Memoization Knapsack Algorithm. |
| [compare.py](compare.py) | Main program that compares both Knapsack algorithms. |
| [pseudopolynomial.py](pseudopolynomial.py) | The Bottom Up Knapsack Algorithm that generates a plot of pseudopolynomial-time. |
