class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_ls = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+ nums[j]== target:
                    new_ls.append(i)
                    new_ls.append(j)

        return new_ls