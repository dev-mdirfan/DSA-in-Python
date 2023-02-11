# APC
ans = []
def helper(arr, start, end):
    if start == end:
        ans.append(ansString[:])
    
    for i in range(len(arr)):
        str1 = arr[i]
        start, end = 0, len(str1)
        if start == 0:
            ansString = ''
        ansString += str1[start]
        helper(arr, start+1, end)

def APC(arr):
    start, end = 0, len(arr)
    helper(arr, start, end)
    return ans


arr = ['ab', 'cd', 'ef']

print(APC(arr))