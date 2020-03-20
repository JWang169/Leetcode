class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        heap = []
        for start, end in slots1:
            heapq.heappush(heap, [start, 0, True])
            heapq.heappush(heap, [end, 0, False])
        
        for start, end in slots2:
            heapq.heappush(heap, [start, 1, True])
            heapq.heappush(heap, [end, 1, False])
        
        t = [-1, -1]
        while heap:
            time, elem, event = heapq.heappop(heap)
            if event:
                t[elem] = time
                continue
            # slot ends, event == False
            if t[0] !=-1 and t[1] != -1 and time - t[0] >= duration and time - t[1] >= duration:
                    return [max(t), max(t) + duration]
            else:
                t[elem] = -1
        return []
                