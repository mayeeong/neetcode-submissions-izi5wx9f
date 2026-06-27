class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check the length of the string
        if len(s) != len(t):
            return False

        dict_s = {}
        for x in s: 
            if x not in dict_s:
                dict_s[x] = 1
            else:
                dict_s[x]+=1
        
        dict_t = {}
        for x in t:
            if x not in dict_t:
                dict_t[x]=1
            else: 
                dict_t[x] +=1
        
        if dict_t != dict_s: 
            return False
        print(dict_t)
        print(dict_s)
        return True
