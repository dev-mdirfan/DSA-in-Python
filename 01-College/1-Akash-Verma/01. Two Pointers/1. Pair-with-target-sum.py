# Brute Force
def solve(arr,target): 
    for i in range(len(arr)): 
        for j in range(i+1,len(arr)): 
            if arr[i]+arr[j]==target: 
                return [i,j] 
    return [-1,-1] 

arr = [2,4,8,7,9,12,14] 
target = 13 
print(solve(arr,target))


# Optimized
def pairSum(arr,target): 
    left = 0 
    right = len(arr)-1 
    
    while left < right: 
        if arr[left] + arr[right] == target: 
            return [left,right] 
        elif arr[left] + arr[right] < target: 
            left += 1 
        else: 
            right -= 1 
    return [-1, -1] 

arr = [1, 3, 5, 6, 8, 9] 
target = 11 
print(pairSum(arr, target)) 
