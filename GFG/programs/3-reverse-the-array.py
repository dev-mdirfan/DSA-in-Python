# Python Slicing - O(n)
def reverseArray(array):
    return array[ : : -1]
array = [3, 5, 7, 9, 10]
print("Original Array: ", array)
result = reverseArray(array)
print("Reversed Array: ",result)