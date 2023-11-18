# Find the maximum average of sum of every sub array of size k.

def maxAvgSubarray(arr, k):
    wStart, wSum, maxAvg = 0, 0, -float('inf')
    for wEnd in range(len(arr)):
        wSum += arr[wEnd]
        if wEnd >= k-1:
            tempAvg = wSum/k
            maxAvg = max(maxAvg, tempAvg)
            wSum -= arr[wStart]
            wStart += 1
    return maxAvg