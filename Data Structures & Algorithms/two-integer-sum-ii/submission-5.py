class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr_1 = 0
        ptr_2 = len(numbers)-1
        
        while ptr_1<ptr_2:
            if numbers[ptr_1]+numbers[ptr_2]>target:
                ptr_2-=1
                continue
            elif numbers[ptr_1]+numbers[ptr_2]<target:
                ptr_1+=1
                continue
            else:
                return [ptr_1+1, ptr_2+1]


        return []
        