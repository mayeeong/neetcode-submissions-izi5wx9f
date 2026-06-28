class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        result = []

        for interval in sorted_intervals: 
            if not result:
                result.append(interval)
            elif result[-1][0]==interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
            elif result[-1][1]>=interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
            
        return result


                

            
        

        