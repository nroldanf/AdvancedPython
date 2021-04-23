'''
Lists performance.
'''
import bisect

def binary_search(l, VAL):
    first_index = 0
    last_index = len(l) - 1
    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2
        if VAL == l[mid_index]:
            break
        else:
            if VAL > l[mid_index]:
                first_index = mid_index + 1
            else:
                first_index = mid_index - 1
    return mid_index

animals = ["dog", "cat", "horse", "rabbit"]
print(animals.index("horse"))

# Search algorithms
l = [9, 18, 18, 19, 29, 42, 56, 61, 88]
print(binary_search(l, 56))

