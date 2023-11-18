# ALL Possible Combinations

def solve(arr):
    # n = len(A)
    # ans = []
    # for i in range(n):
    #     str1 = A[i]
    #     for j in range(i + 1, n):
    #         str2 = A[j]
    #         ans.append()
    
    # Recursion
    self.ans = []
    start, end = 0, 0
    # self.arr = A[:]
    for i in range(len(A)):
        str1 = A[i]
        solve(str1, start, end)
    return self.ans
        