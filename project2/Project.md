# Hybrid Sorting Methods

In class, we’ve seen that divide-and-conquer methods can be used tocreate blazingly fast sorting algorithms such as Mergesort and Quicksort with average-case (some-times worst-case) time complexity Θ(nlogn).  What we haven’t discussed as much is the fact thatfor small arrays,the  elementary  sorting  algorithms  (insertion  sort,  bubble  sort,  selection  sort)aren’t really all that slow, even though they have worst-case time complexity of Θ(n2).  In fact, itcan happen that the best elementary sorting algorithms are actually faster than Mergesort on verysmall arrays.  What can we do with this fact?  We can use Mergesort to handle large arrays, andthen when the arrays in Mergesort’s recursion get small enough, pass them to an elementary sortingalgorithm like Insertion sort to finish up.  This is known ashybrid sortingsince we’re combiningtwo types of sorting algorithm.  If the implementations are good, the combination of the two canbe faster in general than either algorithm individually.  This project will explore this phenomenon.

## Tasks

Create a new sorting algorithmHybridSort(A[n],K)that takes two inputs:

1. A[n]:  A numerical array of lengthn, and•K: A length threshold; note that you must haveK≥1.
1. Ifn≤K, your algorithm should sortit using Insertion Sort.  Ifn > K, your algorithm should sort it using Mergesort.

Since it is a sorting algorithm your algorithm should return or compute a new array that containsexactly the same elements as the input array and is sorted ascending.  Your algorithm may operatein-place or return a new sorted array; the choice is yours.The  high-level  operation  of  your  algorithm  should  work  as  follows,  given  correctly-implementedsubroutinesInsertionSort(A[n])andMerge(B[p],C[q]):