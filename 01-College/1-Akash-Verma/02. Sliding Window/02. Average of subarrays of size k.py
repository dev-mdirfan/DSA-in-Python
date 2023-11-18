# Find the average of sum of every sub array of size k.

def avgSubarray(arr, k):
    wStart, wSum, answer = 0, 0, []
    for wEnd in range(len(arr)):
        wSum += arr[wEnd]
        if wEnd >= k-1:
            answer.append(wSum/k)
            wSum -= arr[wStart]
            wStart += 1
    return answer

arr = [6, 2, 5, 4, 1, 3, 2]
k = 3
print(avgSubarray(arr, k))