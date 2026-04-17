import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dict = {}
        ls = []
        heap = []
        for x in points:
            distance = math.sqrt(x[0]**2 + x[1]**2)
            heapq.heappush(heap, distance)
            dict[tuple(x)] = distance

        i=0
        while i<k:
            x = heapq.heappop(heap)
            keys = next(k for k, v in dict.items() if v == x)
            del dict[keys]
            key = list(keys)
            ls.append(key)
            i+=1

        return ls

