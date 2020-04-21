# Apr 21
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        result = 0
        heap = []
        count = 0
            
        for start, end in intervals:
            heapq.heappush(heap, [start, 1])
            heapq.heappush(heap, [end, 0])
        
        while heap:
            time, status = heapq.heappop(heap)
            if status == 0:
                count -= 1        
            else:
                count += 1 
                result = max(result, count)
        
        return result
                
        
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        result = 0
        count = 0
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, 0))
        
        events.sort()
        # events = sorted(events, key=(lambda x: [x[0], x[1]]))
        for event in events:
            if event[1] == 1:
                count += 1 
            else:
                count -= 1 
            result = max(count, result)
        
        return result