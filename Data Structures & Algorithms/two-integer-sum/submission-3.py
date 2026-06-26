class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if d.get(num) != None:
                return [d[num], i]
            else:
                d[target-num] = i 
                
