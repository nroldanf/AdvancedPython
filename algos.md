# Algorithms reviewing

## Binary Search

__Complexity:__ O(log n)

The list has to be ordered.
1. Split in two the list.
2. Compared the value with the middle value.
    - If it is the value we are looking for, return.
    - If not, compare, greater or smaller?. If greater
    look for the right side, otherwise, look for the left.
3. Repeat 1 and 2 recursively until you find the value.
