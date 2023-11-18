#  TC : O(2^m)
class Solution1:
    def helper(self, nums, multipliers, operation, left, right):
        if operation == len(multipliers):
            return 0
        leftAns = nums[left] * multipliers[operation] + self.helper(nums, multipliers, operation + 1, left + 1, right)
        rightAns = nums[right] * multipliers[operation] + self.helper(nums, multipliers, operation + 1, left, right - 1)
        return max(leftAns, rightAns)
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        return self.helper(nums, multipliers, 0, 0, len(nums)-1)


#  TC : O(2^m) 2 states
class Solution2:
    def helper(self, nums, multipliers, operation, left):
        if operation == len(multipliers):
            return 0
        leftAns = nums[left] * multipliers[operation] + self.helper(nums, multipliers, operation + 1, left + 1)
        rightAns = nums[(len(nums) - 1) - (operation - left)] * multipliers[operation] + self.helper(nums, multipliers, operation + 1, left,)
        return max(leftAns, rightAns)
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        return self.helper(nums, multipliers, 0, 0)


#  TC : O(2^m) 2 states
from math import inf
class Solution3:
    def helper(self, nums, multipliers, operation, left, dp):
        if operation == len(multipliers):
            return 0
        if dp[operation][left] != -1:
            return dp[operation][left]
        leftAns = nums[left] * multipliers[operation] + self.helper(nums, multipliers, operation + 1, left + 1, dp)
        rightAns = nums[(len(nums) - 1) - (operation - left)] * multipliers[operation] + self.helper(nums, multipliers, operation + 1, left, dp)
        dp[operation][left] = max(leftAns, rightAns)
        return dp[operation][left]
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # dp = [ [-inf for i in range(m)]] * m
        dp=[[ -1 ] * len(multipliers) for i in range(len(nums))]
        # dp=[[-inf]*m for i in range(n)]
        # print(dp)
        return self.helper(nums, multipliers, 0, 0, dp)


#  MLE 
from math import inf
class Solution4:
    def helper(self, nums, multipliers, operation, left, dp):
        if operation == len(multipliers):
            return 0
        if dp[operation][left] != -inf:
            return dp[operation][left]
        leftAns = nums[left] * multipliers[operation] + self.helper(nums, multipliers, operation + 1, left + 1, dp)
        rightAns = nums[(len(nums) - 1) - (operation - left)] * multipliers[operation] + self.helper(nums, multipliers, operation + 1, left, dp)
        dp[operation][left] = max(leftAns, rightAns)
        return dp[operation][left]
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        dp=[[ -inf ] * len(multipliers) for i in range(len(nums))]
        return self.helper(nums, multipliers, 0, 0, dp)


#  Tabulation
from math import inf
class Solution5:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        dp=[[ 0 ] * (len(multipliers) + 1) for i in range(len(multipliers) + 1)]
        for operation in range(len(multipliers) - 1, -1, -1):
            for left in range(operation, -1, -1):
                leftAns = nums[left] * multipliers[operation] + dp[operation + 1][left + 1]
                rightAns = nums[(len(nums) - 1) - (operation - left)] * multipliers[operation] + dp[operation + 1][left]
                dp[operation][left] = max(leftAns, rightAns)
        return dp[0][0]


#  Tabulation
from math import inf
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        dp = [ 0 ] * (m + 1)
        for operation in range(m):
            mult = multipliers[m - 1 - operation]
            # at round m, we  pick the m-th multiplier
            # at round m - 1, we pick the (m - 1) - ith multiplier
            # at round m - 2, we pick the (m - 2) - ith multiplier
            # and so on ... 
            for left in range(m - operation):
                # how many elements we need to process? 
                # at round m, there are m elements
                # at round m - 1, there are m - 1 elements
                # at round m - 2, there are m - 2 elements
                # and so on ...
                leftAns = nums[left] * mult + dp[left + 1]
                rightAns = nums[left + len(nums) - (m - operation)] * mult + dp[left]
                dp[left] = max(leftAns, rightAns)
        return dp[0]