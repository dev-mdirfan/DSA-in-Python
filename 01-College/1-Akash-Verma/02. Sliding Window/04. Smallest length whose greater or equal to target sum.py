# Given an array and a target sum
# Calculate the smallest length of the subarray whose sum is greater than or equal to the target sum.

def smallestSubarray(arr, target):
    wStart, wSum, minLength = 0, 0, float('inf')
    for wEnd in range(len(arr)):
        wSum += arr[wEnd]
        while wSum >= target:
            minLength = min(minLength, wEnd-wStart+1)
            wSum -= arr[wStart]
            wStart += 1
    if minLength == float('inf'):
        # return 0
        return -1
    return minLength

arr = [2, 1, 4, 6, 2, 6, 5, 3, 4]
print(smallestSubarray(arr, 9))
