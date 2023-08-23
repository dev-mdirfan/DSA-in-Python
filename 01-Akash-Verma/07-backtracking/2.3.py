# APC
ans = []
temp = ''
def helper(arr, start, end):
    global temp
    if start == end:
        # print(arr[start])
        ans.append(temp)
        # i = 0
        # temp = ''
    
    for i in range(start, end):
        for j in range(len(arr[i])):
            # ans.append(arr[i][j])
            temp += arr[i][j]
            helper(arr, start+1, end)
            # print(arr[i][j])
            # temp = ''
            temp = temp[ : j - 1]
            # print(temp)

def APC(arr):
    start, end = 0, len(arr)
    # temp = ''
    helper(arr, start, end)
    return ans


arr = ['ab', 'cd', 'ef']

print(APC(arr))