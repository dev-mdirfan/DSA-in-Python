# Brute Force
def squareArr(arr): 
    ans = [] 
    for i in arr: 
        ans.append(i*i) 
    return sorted(ans) 

arr = [-5, -4, -1, 0, 2, 3, 4] 
print(squareArr(arr))


# Optimal Solution
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


# Optimal Solution 2
def squareArr(arr): 
    ans = [] 
    left, right = 0, len(arr)-1 
    while left<=right: 
        l = arr[left]*arr[left] 
        r = arr[right]*arr[right] 
        if l>r: 
            ans.insert(0,l) 
            left += 1 
        else: 
            ans.insert(0,r) 
            right -= 1 
    return ans 

arr = [-5, -4, -1, 0, 2, 3, 4] 
print(squareArr(arr))