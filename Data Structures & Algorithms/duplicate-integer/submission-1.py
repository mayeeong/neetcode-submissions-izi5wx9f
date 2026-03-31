class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_ls = []
        for x in nums:
            if x not in new_ls:
                new_ls.append(x)
            else:
                return True
        print(new_ls)
            
        return False
        