ans = []

def permute(arr, start, end):
    if start == end:
        ans.append(arr[:])
    else:
        for index in range(start, end):
            arr[start], arr[index] = arr[index], arr[start]
            permute(arr, start + 1, end)
            arr[start], arr[index] = arr[index], arr[start]

arr = list('ABC')
start, end = 0, len(arr)
permute(arr, start, end)
print([''.join(x) for x in ans])