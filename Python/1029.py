import heapq 
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        heap = []
        for c1, c2 in costs:
            dc = c1 - c2
            heapq.heappush(heap, [dc, c1, c2])
        result = 0 
        for i in range(len(costs) // 2):
            dc, c1, c2 = heapq.heappop(heap)
            result += c1
        
        for i in range(len(heap)):
            result += heap[i][2]
        return result