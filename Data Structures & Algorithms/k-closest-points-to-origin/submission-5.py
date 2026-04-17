import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ls = []
        heap = []
        for x in points:
            distance = math.sqrt(x[0]**2 + x[1]**2)
            heapq.heappush(heap, (distance, x))

        i=0
        while i<k:
            dist, point = heapq.heappop(heap)
            ls.append(point)
            i+=1

        return ls

