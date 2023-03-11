# Recursive - O(n) and call stack
def reverseArray(array, start, end):
    if start >= end:
        return None
    else:
        array[start], array[end] = array[end], array[start]
        return reverseArray(array, start+1, end-1)

array = [9, 3, 4, 7, 8, 1]
start, end = 0, len(array)-1
print("Original Array: ", array)
reverseArray(array, start, end)
print("Reversed Array: ",array)