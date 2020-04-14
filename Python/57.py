class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        start, end = newInterval 
        result = []
        while i < len(intervals):
            if start <= intervals[i][1]:
                # no overlap, insert newInterval in front of i
                if end < intervals[i][0]:
                    break
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
            else:
                result.append(intervals[i])
            i += 1
        
        result.append([start, end])
        result += intervals[i:]
        return result