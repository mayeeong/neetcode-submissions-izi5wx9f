class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_window = len(s1)
        target = sorted(s1)
        print(target)

        for start in range(len(s2)-len_window +1):
            s2_check = sorted(s2[start:start+len_window]) 
            if s2_check == target:
                return True
        
        return False
            
            

        