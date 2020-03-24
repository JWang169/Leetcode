"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        heap = []
        for i in range(len(intervals)):
            pairs = intervals[i]
            if pairs:
                # idx: index of current list 
                # i: index of intervals 
                heapq.heappush(heap, [pairs[0].start, pairs[0].end, 0, i])
        
        if len(heap) == 0:
            return []
        result = []
        start, end = heap[0][0], heap[0][1]
        while heap:
            curStart, curEnd, idx, i = heapq.heappop(heap)
            if curStart > end:
                node = Interval(start, end)
                result.append(node)
                start = curStart
                end = curEnd 
            else:
                end = max(end, curEnd)
            
            if len(intervals[i]) > idx + 1:
                pairs = intervals[i][idx + 1]
                heapq.heappush(heap, [pairs.start, pairs.end, idx + 1, i])
        result.append(Interval(start, end))
        
        return result
        