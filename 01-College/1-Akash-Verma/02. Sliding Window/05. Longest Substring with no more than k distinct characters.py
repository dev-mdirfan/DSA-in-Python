# Find the longest substring with no more than k distinct characters otherwise return -1

# Time: O(n^2) | Space: O(n) | Brute Force
def longestSubstring1(arr, k):
    longest = 0
    for i in range(len(arr)):
        wSum = {}
        for j in range(i, len(arr)):
            if arr[j] not in wSum:
                wSum[arr[j]] = 0
            wSum[arr[j]] += 1
            if len(wSum) <= k:
                longest = max(longest, j-i+1)
    return longest

def longestSubstring2(arr, k):
    def isValid(arr, k):
        return len(set(arr)) <= k
    
    maxLength = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if isValid(arr[i:j+1], k):
                maxLength = max(maxLength, j-i+1)
    return maxLength

def longestSubstring3(arr, k):
    wStart, wEnd, maxLen = 0, 0, 0
    for wEnd in range(len(arr)):
        charSet = set()
        for wStart in range(wEnd, -1, -1):
            charSet.add(arr[wStart])
            if len(charSet) > k:
                break
            maxLen = max(maxLen, wEnd-wStart+1)
    return maxLen

# Sliding Window Time: O(N) | Space: O(N)
def longestSubstring(arr, k):
    wStart, wSum, longest = 0, {}, 0
    for wEnd in range(len(arr)):
        if arr[wEnd] not in wSum:
            wSum[arr[wEnd]] = 0
        wSum[arr[wEnd]] += 1
        while len(wSum) > k:
            wSum[arr[wStart]] -= 1
            if wSum[arr[wStart]] == 0:
                del wSum[arr[wStart]]
            wStart += 1
        longest = max(longest, wEnd-wStart+1)
    return longest

arr = "araaci"
k = 2
print(longestSubstring(arr, k))

arr = 'abcdaebbbaed'
k = 3
print(longestSubstring(arr, k))

arr = 'aabacbebebe'
k = 3
print(longestSubstring(arr, k))

arr = 'aabacbebebe'
k = 5
print(longestSubstring(arr, k)) # answer is -1


