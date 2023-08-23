# T.C: O(n log n)
# S.C: O(1)

def squareArr(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] ** 2
    return sorted(arr)

arr = [-5, -4, -1, 0, 2, 3, 4]
print(squareArr(arr))