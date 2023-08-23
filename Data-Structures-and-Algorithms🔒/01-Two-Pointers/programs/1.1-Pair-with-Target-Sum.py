# T.C: O(n)
def pairSum(arr,target):
    left = 0
    right = len(arr)-1
    while left < right:
        Sum = arr[left] + arr[right]
        if Sum == target:
            return [left,right]
        elif Sum < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]

arr = [1, 3, 5, 6, 8, 9]
target = 11
print(pairSum(arr, target))