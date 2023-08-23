# T.C: O(n)
# S.C: O(1)

def square(arr):
    left,right = 0, len(arr)-1
    index = len(arr)-1
    ans = [0]*len(arr)
    while left<=right:
        lsquare = arr[left]**2
        rsquare = arr[right]**2
        if lsquare > rsquare:
            ans[index] = lsquare
            left += 1
        else:
            ans[index] = rsquare
            right -= 1
        index -= 1
    return ans

arr = [-5, -4, -2, 0, 1, 3, 4]
print(square(arr))
