# Iterative - O(n)
def reverseArray(array):
    start, end = 0, len(array)-1
    # you don't need to reverse at the equal index on odd length
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

array = [6, 5, 4, 7, 8, 2]
print("Original Array: ",array)
reverseArray(array)
print("Reverse Array: ",array)
