class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for x in stones:
            heapq.heappush(heap, -x)

        while len(heap)>1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            sub = x-y
            if sub>0:
                heapq.heappush(heap, -sub)
            continue

        if len(heap)>0:
            return -heap[0]

        else:
            return 0
        