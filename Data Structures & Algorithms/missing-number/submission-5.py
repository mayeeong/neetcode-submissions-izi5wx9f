class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = max(nums)
        for i in range(x):
            if i not in nums:
                return i
        return x+1
        