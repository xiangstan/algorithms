# Homework 7 Scheduling Compatible Intervals
# 
# Author: Xiang Shan Tan
#
# This program contains three different implementations of the Scheduling Compatible Intervals.
#   Earliest start first,
#   Shortest duration first,
#   Earliest finish first
#
# Ths sample jobs are (start time, end time): [(1, 3), (2, 5), (4, 5)]


import numpy as np

# Earliest start first
def EarlistStartFirst (start, end) :
    # generate an empty array to store selected jobs
    jobs = []
    # sort end array order by started time
    queue = np.argsort(start)
    timer = 0
    for i in queue :
        if start[i] >= timer :
            jobs.append(i)
            timer = end[i]
    return jobs, timer

# Shortest duration first
def ShortestDurFirst (start, end) :
    # generate an empty array to store selected jobs
    temp = []
    sorts = []
    # generate an array from with each job's duration
    for i in range(len(end)) :
        temp.append(end[i] - start[i])

    # sort duration array order by shortest duration
    queue = np.argsort(temp)
    # add the job with shortest duration into the job array
    sorts.append(queue[0])
    # record its start and end time for comparison later
    begin = start[sorts[0]]
    last = end[sorts[0]]
    # set the timer to the first job's end time
    timer = last
    # loop through the entire queue
    for i in queue :
        # if the end time of the selected job is earlier than the earliest saved jobs
        if end[i] < begin :
            sorts.append(i)
            begin = start[i]
        # if the start time of the selected job is later than the latest saved jobs
        elif start[i] > last :
            sorts.append(i)
            last = end[i]
            timer = end[i]
    # sort the job array
    jobs = sorted(sorts)
    return jobs, timer
 
# Earliest finish first
def EarlistFinishFirst (start, end) :
    # generate an empty array to store selected jobs
    jobs = []
    # sort end array order by finished time
    queue = np.argsort(end)
    timer = 0
    for i in queue :
        if start[i] >= timer :
            jobs.append(i)
            timer = end[i]
    return jobs, timer

def main() :
    start = [1, 2, 4]
    end = [3, 5, 5]
    print("Earlist Started First:")
    jobs, completed_timer = EarlistStartFirst(start, end)
    print(f"Job Queue: {jobs}, completed time: {completed_timer}\n")

    print("Shortest Duration First:")
    jobs, completed_timer = ShortestDurFirst(start, end)
    print(f"Job Queue: {jobs}, completed time: {completed_timer}\n")

    print("Earlist Finished First:")
    jobs, completed_timer = EarlistFinishFirst(start, end)
    print(f"Job Queue: {jobs}, completed time: {completed_timer}\n")

if __name__ == "__main__":
    main()