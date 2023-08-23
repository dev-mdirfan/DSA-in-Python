# O(n ^ 3) time and O(1) extra space
class Solution1:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    # We have the triplet (i, j, k)
                    # This will generate every possible triplets : That is why it is Brute Force
                    if self.isValid(i, j, k, nums, diff):
                        count += 1
        return count
    # def isValid(self, i, j, k, nums, diff):
    #     if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
    #         return True
    #     else:
    #         return False

    def isValid(self, i, j, k, nums, diff):
        return nums[j] - nums[i] == diff and nums[k] - nums[j] == diff
