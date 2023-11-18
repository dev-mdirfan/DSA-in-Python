# Sum of subarrays of size k
# You have given an array and an integer k. We need to find sum of all subarrays of size k.

# O(n*k) Brute Force
def subarraySum1(arr, k):
    ans = []
    n = len(arr)
    for i in range(n-k+1):
        s = 0
        for j in range(i, i+k):
            s += arr[j]
        ans.append(s)
    return ans


# Time: O(n*k) using slicing
def subarraySum2(arr, k):
    i, n = 0, len(arr)
    ans = []
    while i < n-k+1:
        s = sum(arr[i : i+k])
        ans.append(s)
        i += 1
    return ans

'''
In the above approaches the problem is that we are calculating the sum of subarray again and again. We can optimize it by using sliding window technique.
'''

def subarraySum3(arr, k):
    ans = []
    wSum, ws, we = 0, 0, 0
    while we < len(arr):
        if we - ws + 1 <= k:
            wSum += arr[we]
        else:
            ans.append(wSum)
            wSum -= arr[ws]
            wSum += arr[we]
            ws += 1
        we += 1
    ans.append(wSum)
    return ans

def subarraySum4(arr, k):
    ans = []
    wSum, ws, we = 0, 0, 0
    while we < len(arr):
        wSum += arr[we]
        if we-ws+1 < k:
            we += 1
        elif we-ws+1 == k:
            print(wSum)
            wSum -= arr[ws]
            ws += 1
            we += 1
    return ans

# Time: O(n) using sliding window
def subarraySum5(arr, k):
    i, n = 0, len(arr)
    ans = []
    s = sum(arr[:k])
    ans.append(s)
    while i < n-k:
        s = s - arr[i] + arr[i+k]
        ans.append(s)
        i += 1
    return ans


def subarraySum6(arr, k):
    wStart = 0
    wSum = 0
    ans = []
    for wEnd in range(len(arr)):
        wSum += arr[wEnd]
        # if wEnd >= k-1:
        if wEnd-wStart+1 == k:
            ans.append(wSum)
            wSum -= arr[wStart]
            wStart += 1
    return ans

# Time: O(n) using prefix sum
# Space: O(n)
def subarraySum(arr, k):
    prefixSum, ans = [0], []
    for i in range(len(arr)):
        prefixSum.append(prefixSum[-1] + arr[i])
    for i in range(len(arr)-k+1):
        s = prefixSum[i+k] - prefixSum[i]
        ans.append(s)
    return ans

arr = [6, 2, 5, 4, 1, 3, 2]
k = 3
print(subarraySum(arr, k))