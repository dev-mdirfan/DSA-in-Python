class solution:
    def __init__(self, nums) -> None:
        result = self.solve(nums)
        print([''.join(string) for string in result])
    def permute(self, arr, start, end) -> None:
        if start == end:
            self.ans.append(arr[:])
        else:
            for index in range(start, end):
                arr[start], arr[index] = arr[index], arr[start]
                self.permute(arr, start + 1, end)
                arr[start], arr[index] = arr[index], arr[start]
    
    def solve(self, nums) -> list:
        arr = list(nums)
        self.ans = []
        start, end = 0, len(arr)
        self.permute(arr, start, end)
        return self.ans

nums = 'ABC'
solution(nums)

