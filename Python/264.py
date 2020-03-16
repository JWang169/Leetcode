import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = set()
        for _ in range(n - 1):
            num = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                ugly = num * factor 
                if ugly not in seen:
                    heapq.heappush(heap, ugly)
                    seen.add(ugly)
        return heapq.heappop(heap)