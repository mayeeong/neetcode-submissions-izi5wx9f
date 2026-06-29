class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        res = 0 
        
        for right in range(len(s)):
            # means it is a duplicate
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])

            # calculate the total 
            res = max(res, right-left+1) #current length 

        return res

                


                        