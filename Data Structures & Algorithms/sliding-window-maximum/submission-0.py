class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ls = []
        i=0
        last_node = len(nums)-k+1

        while i<last_node:
            max = nums[i]
            count = 0
            j= i
            # The last node to check will be the total len - k 
            while count<k:
                if nums[j]>max:
                    max = nums[j]

                j+=1
                count+=1


            ls.append(max)  

            i+=1      

        return ls
        