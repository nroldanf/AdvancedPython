#

- Can retrieve data from specific position at O(1)!
- Lists are dynamic arrays while tuples are static arrays.
- Linear search iterate over every element in the array. (O(n) performance) list.index() uses this algorithm.
- Hash tables (which are fundamental data structure powering dictionaries and sets) solves this problem in O(1) time.
- Python have a built-in sort function that uses Tim Sort (O(n) in the best case, and O(n * log(n)) in the worst case). Using heuristics guess which algorithm will perform best
- Converting to a dictionary can take O(n) time.

- Tuples are cached by Python runtime, which means that we don't need to talk to the kernel to reserve memory every time we want to use one (resource caching).
- Tuples inmutability makes it a very lightweight data structure.
- When a list of length N is created extra space is allocated in order to provide extra space for appendings M. Then the data of the old list is copied to the new list, and the old list is destroyed. This __overallocation__ happens only in the first append. When N == M, the new list is created, with more extra space. This is important since memory copies can be quite expensive.
- Tuples can be concatenated, and unlike lists, do not allocate extra space for the resulting tuple. When a list of size 100M is created with any append, it actually uses ~112M, while a tuple will only use exactly 100M. Even if we create a list __without append__, a tuple of the same size will be smaller in memory, having a list to store its length.
- Tuples can be created easily and quickly without needing to communicate with the OS. Instantiating a tuple can be 5.1x faster than instantiating a list.

N 0 1-4 5-8 9-16 17-25 26-35 36-46 ... 991-1120

M 0 4 8 16 25 35 46 ... 1120


When we want to create an array (tuple or list):
1. Have to allocate a block of system memory
