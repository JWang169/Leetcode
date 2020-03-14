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