class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}

        for num in nums:
            if num not in dict:
                dict[num] = 1
            dict[num]+=1

        ls = []
        i = 0 
        while i<k:
            largest_key = max(dict, key= lambda x: dict[x])
            ls.append(largest_key)
            del dict[largest_key]
            i+=1

        return ls
        