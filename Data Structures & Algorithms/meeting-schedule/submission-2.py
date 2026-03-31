"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i].start <= right[j].start:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result


    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0: 
            return True
        
        intervals = self.merge_sort(intervals)
        len_intervals = len(intervals)
        i=0

        while i<len_intervals:
            if i == len_intervals - 1:
                return True
            
            if intervals[i].end>intervals[i+1].start:
                return False 
            
            i+=1

        return False


