class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # safety check 
        if len(s)!=len(t):
            return False
        
        dictionary_s = {}

        #create dictionary for s: 
        for c in s: 
            if c not in dictionary_s:
                dictionary_s[c] = 1
            else: 
                 dictionary_s[c]+=1

        print(dictionary_s)

        dictionary_t={}

        #create dictionary for t: 
        for x in t:
            if x not in dictionary_t:
                 dictionary_t[x]=1
            else:
                 dictionary_t[x]+=1
        
        if dictionary_t == dictionary_s:
             return True
        
        return False