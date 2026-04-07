class Solution:
    def isValid(self, s: str) -> bool:
        # Make a dictionary to match the parenthese 
        matching = {')':'(', ']':'[', '}':'{'}
        
        # Initialise stack 
        stack = []

        if len(s)==1 or len(s)==0:
            return False

        # start loop
        i = 0
        while i<len(s):
            if s[-1] in '({[':
                return False 

            if s[i] in '{([':
                stack.append(s[i])
            
            if s[i] in '}])':
                if not stack:
                    return False

                if stack[-1]!= matching[s[i]]:
                    return False

                stack.pop()
            
            i+=1
        
        return len(stack)==0 