from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for word in strs:
            key = "".join(sorted(word))
            if key not in groups:
                groups[key] = []
            
            groups[key].append(word)
        
        print(groups)

        return list(groups.values())

        
        
        
        