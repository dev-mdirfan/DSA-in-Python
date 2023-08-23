def tripletZero(arr):
    n = len(arr)
    ans = set()
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i] + arr[j] + arr[k] == 0:
                    ans.add((arr[i], arr[j], arr[k]))
    return ans

arr = [-3, 0, 1, 2, -1, 1, -2]
print(tripletZero(arr))
