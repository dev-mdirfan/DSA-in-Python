# T.C: O(n^2)
def solve(arr,target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return [-1, -1]

arr = [2, 4, 8, 7, 9, 12, 14]
target = 13
print(solve(arr, target))
