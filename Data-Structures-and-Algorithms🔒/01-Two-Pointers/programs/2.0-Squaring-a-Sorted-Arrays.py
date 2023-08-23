# T.C: O(n log n)
# S.C: O(n)
def squareArr(arr):
    ans = []
    for i in arr:
        ans.append(i*i)
    return sorted(ans)

arr = [-5, -4, -1, 0, 2, 3, 4]
print(squareArr(arr))