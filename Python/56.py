class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heap = []
        for start, end in intervals:
            heapq.heappush(heap, (start, 0))
            heapq.heappush(heap, (end, 1))
        results = []
        stack = []
        while heap:
            num, state = heapq.heappop(heap)
            if state == 0:
                stack.append(num)
            else:
                first = stack.pop()
            if not stack:
                results.append([first, num])
                    
        return results
                    