class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        dic = {}
        for x in n:
            if x in dic:
                dic[x] +=1
            else:
                dic[x] = 1

        return dic.get('1',0)
        