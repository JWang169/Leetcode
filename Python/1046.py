class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for num in stones:
            heapq.heappush(heap, -num)
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            n = x - y
            if n > 0:
                heapq.heappush(heap, -n)
        
        if heap:
            return -heapq.heappop(heap)
        return 0        
        