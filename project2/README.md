# Hybrid Sorting Methods

In class, we've seen that divide-and-conquer methods can be used tocreate blazingly fast sorting algorithms such as Mergesort and Quicksort with average-case (some-times worst-case) time complexity Θ(nlogn).  What we haven’t discussed as much is the fact thatfor small arrays,the  elementary  sorting  algorithms  (insertion  sort,  bubble  sort,  selection  sort)aren’t really all that slow, even though they have worst-case time complexity of Θ(n2).  In fact, itcan happen that the best elementary sorting algorithms are actually faster than Mergesort on verysmall arrays.  What can we do with this fact?  We can use Mergesort to handle large arrays, andthen when the arrays in Mergesort’s recursion get small enough, pass them to an elementary sortingalgorithm like Insertion sort to finish up.  This is known ashybrid sortingsince we’re combiningtwo types of sorting algorithm.  If the implementations are good, the combination of the two canbe faster in general than either algorithm individually.  This project will explore this phenomenon.

## Deliverables

Create a new sorting algorithmHybridSort(A[n], K) that takes two inputs.

1. Implementation's code and verfication of correctness.
1. A plot showing the average run time of the algorithm as a function of K, with a separate trace for at least 5 representative value of n.
1. A plot showing the optimal value of K as a function of array length n. Explain why the relationship between an and optimal K is the way that it is.
1. Repeat **Deliverables** 2 and 3; however, this time, test algorithm only on sorted array. How do the results differ from what reported in **Deliverables** 2 and 3? Explain these differences to the best of ability.

## Files

| Filename | Description |
|--- |--- |
| [hybridsort.py](hybridsort.py) | The hybrid sorting algorithm. |
| [insertionsort.py](insertionsort.py) | The insertion sort algorithm. |
| [mergesort2.py](mergesort2.py) | This merge sort algorithm. It splits the given array to two subarrays each recursive call. |
| [sortedhybrid.py](sortedhybrid.py) | This is the hybrid sorting algorithm with only sorted array as input data. |
| [validate.py](validate.py) | This program validated hybrid sorting alogirthm gives same results as Python built-in sorting function. |