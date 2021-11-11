# Scheduling Compatible Intervals:

Suppose you have a server that can only process one job at
a time, and you have n potential jobs that could be scheduled on it. Each job has a specific
start time and end time, and your task is to design an algorithm to determine the largest
possible number of jobs that can be scheduled. Specifically, for each i ∈ {1, . . . , n}, job
i needs to start at time ai and will run until time bi. Your algorithm’s input should be an
array of start times and an array of end times; your algorithm should determine the largest
possible number of jobs that can be scheduled and a list of those jobs’ indices.

Given the following start/end times: [(1, 3), (2, 5), (4, 5)]

## Deliverable

Design three possible greedy algorithms for this problem; the algorithms should be based on

1. earliest start first,
1. shortest duration first,
1. earliest finish first.

## Files

| Filename | Description |
|--- |--- |
| [schedule.py](schedule.py) | All three Scheduling Compatible Intervals Algorithms. |
