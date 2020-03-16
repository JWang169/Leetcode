import heapq 
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        results = []
        heap = []
        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(heap, (dist, x, y))
        for i in range(K):
            point = heapq.heappop(heap)
            results.append([point[1], point[2]])
        return results