# Brute Force: O(N^3) time | O(1) space
def countTriplet(arr, target): 
    count = 0
    triplets = []
    for i in range(len(arr)): 
        for j in range(i+1, len(arr)): 
            for k in range(j+1, len(arr)): 
                if arr[i] + arr[j] + arr[k] < target:
                    triplets.append((arr[i], arr[j], arr[k]))
                    count += 1 
    return count, triplets

arr = [-1, 4, 2, 1, 3] 
target = 5 
print(countTriplet(arr, target))


def tripletSum(arr, target):
    arr.sort()
    count = 0
    triplets = set()
    for i in range(len(arr)-2):
        count += findPair(arr, arr[i], i+1, target, triplets)
    return (count, triplets)


def findPair(arr, first, start, target, triplets):
    count = 0
    end = len(arr)-1
    while start < end:
        if first + arr[start] + arr[end] < target:
            for i in range(start+1, end+1):     # all elements between start and end will give a sum less than target
                triplets.add((first, arr[start], arr[i]))
            count += end - start
            start += 1
        else:
            end -= 1
    return count

arr = [-1, 0, 2, 3]
target = 3
print(tripletSum(arr, target))

arr = [-1, 4, 2, 1, 3]
target = 5
print(tripletSum(arr, target))