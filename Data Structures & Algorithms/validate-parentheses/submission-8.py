class Solution:
    def isValid(self, s: str) -> bool:
        # Make a dictionary for each one
        while '()' in s or '[]' in s or '{}'in s:
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
        
        return s == ''