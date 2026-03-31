class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = {}
        for num in nums:
            if num in x: 
                x[num] +=1
            else:
                x[num]= 1

        for key, values in x.items(): 
            if x[key] == 1:
                return key

        

        