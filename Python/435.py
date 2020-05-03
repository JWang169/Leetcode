class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        count = 0
        intervals.sort()
        left, right = intervals[0]
        for start, end in intervals[1:]:
            if start < right:
                count += 1 
                right = min(right, end)
            else:
                right = end 
        return count
            
        
        