
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        x1 = newInterval[0]
        x2 = newInterval[1]
        result = []

        for interval in intervals:            
            #case 1: 
            if interval[1]< x1:
                result.append(interval)
            elif interval[0]> x2:
                result.append(newInterval)
                newInterval = interval 
            else:
                newInterval[0]= min(x1,interval[0])
                newInterval[1]= max(x2, interval[1])
                x1 = newInterval[0]
                x2 = newInterval[1]                  
            

        result.append(newInterval)
        return result
            
            
            
            
    
