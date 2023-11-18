# arr = [4, 5, 7, 8, 5, 3]
# arr = [10, 11, 23, 23, 23]
# arr = [1, 2, 2, 3, 4]
# arr = [2, 1, 1, 3]
# arr = [2, 1, 3]
# [19, 28, 14, 20, 1, 3, 9, 5, 3]
import math

arr = [19, 28, 14, 20, 1, 3, 9, 5, 3]
n = len(arr)
ans = [0]*(n+1)
ans[0] = 0
for i in range(n):
    if arr[i]==1:
        ans[i+1] = -1
    else:
        ans[i+1] = ans[i]+1
    for j in range(1, i+1):
        gcd = math.gcd(arr[j-1], arr[i])
        if gcd>1:
            ans[i+1] = min(ans[i+1], ans[j-1] + 1)
        else:
            ans[i+1] = -1
    print(ans)

print(ans[-1])