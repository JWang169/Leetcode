import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        count = 0
        visited = set()
        heap = []
        mappings = collections.defaultdict(dict)
        for src, des, time in times:
            mappings[src][des] = time 
        
        heapq.heappush(heap, [0, K])
        while heap:
            cost, k = heapq.heappop(heap)
            if k not in visited:
                visited.add(k)
                if k in mappings:
                    for nxt in mappings[k]:
                        heapq.heappush(heap, [mappings[k][nxt] + cost, nxt])
            
            if len(visited) == N:
                return cost
        return -1 