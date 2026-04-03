class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ptr_1 = 0
        ptr_2 = 1
        ptr_3 = len(nums) - 1
        ls = []

        if all(x == 0 for x in nums):
            ls.append([0, 0, 0])
            return ls

        while ptr_1 < len(nums) - 2:
            target = -nums[ptr_1]
            ls_1 = []

            while ptr_2 < ptr_3:
                if nums[ptr_2] + nums[ptr_3] > target:
                    ptr_3 -= 1
                elif nums[ptr_2] + nums[ptr_3] < target:
                    ptr_2 += 1
                else:
                    ls_1.append([nums[ptr_1], nums[ptr_2], nums[ptr_3]])
                    ptr_2 += 1  # keep going, don't break
                    ptr_3 -= 1

            for triplet in ls_1:
                if triplet not in ls:
                    ls.append(triplet)

            ptr_1 += 1
            ptr_2 = ptr_1 + 1
            ptr_3 = len(nums) - 1

        return ls

        