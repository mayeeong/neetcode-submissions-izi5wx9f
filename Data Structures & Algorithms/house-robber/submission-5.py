class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2:
            return max(nums)

        x = [0]*(n+1)
        x[1] = nums[0]
        for i in range(2, n+1):
            x[i] = max(x[i-1], x[i-2]+nums[i-1])

        return x[n]
        