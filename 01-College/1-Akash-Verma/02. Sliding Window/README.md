# 02. Sliding Window

### Approach 2: 

```py
def subarray(arr, k):
    ws = 0
    wsum = 0
    ans = []
    for we in range(len(arr)):
        wsum += arr[we]
        if we-ws+1==k:
            ans.append(arr[we])
            wsum -=arr[ws]
            ws+=1
    return ans
```
