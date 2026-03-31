from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ls = []
        groups = {}
        for word in strs:
            key = "".join(sorted(word)) #sort word alphabetically
            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        for key, value in groups.items():
            ls.append(groups[key])

        return ls

        
        
        
        