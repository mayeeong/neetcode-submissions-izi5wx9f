class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        i=0
        heap = []

        if len(nums) ==1 and k==1:
            return nums[0]

        for x in nums:
            heapq.heappush(heap, -x)


        while i<k:
            if i == k-1:
                return -heapq.heappop(heap)
            -heapq.heappop(heap)
            i+=1