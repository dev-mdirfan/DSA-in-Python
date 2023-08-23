# Sliding Window

## Q.1) Sum of subarrays of size k
- You have given an array and an integer k.
- We need to find sum of all subarrays of size k. 

### Approach  1: Brute Force
```py
def subarraySum(arr,k):
    ans = []
    n = len(arr)
    for i in range(n-k-1):
        sum = 0
        for j in range(i,i+k):
            sum+=arr[j]
        ans.append(sum)
    return ans
```
- ***Time Complexity :*** O(n*k)


### Approach 2: sliding window

```py
def subarray(arr, k):
    ws = 0
    wsum = 0
    ans = []
    for we in range(len(arr)):
        wsum +=arr[we]
        if we-ws+1==k:
            ans.append(arr[we])
            wsum -=arr[ws]
            ws+=1
    return ans
```














## Questions :

| S.No | Question                                                       | Related Topics |
| ---- | -------------------------------------------------------------- | -------------- |
| 1.   | [Smallest subarray with sum greater than k](https://practice.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1) | `Sliding Window`, `Prefix Sum`    |
| 2.   | [Two Sum (Not sorted)](https://leetcode.com/problems/two-sum/) | `Hash Map`     |