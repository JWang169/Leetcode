import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        mappings = collections.defaultdict(dict)
        for s, d, p in flights:
            mappings[s][d] = p
        # cost, start, k 
        heap = [[0, src, K + 1]]
        while heap:
            cost, s, k = heapq.heappop(heap)
            if s == dst:
                return cost
            if k > 0 and s in mappings:
                for nxt in mappings[s]: 
                    heapq.heappush(heap, [cost+mappings[s][nxt], nxt, k - 1])
        return -1 
            

# dfs dijkstra's
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        prices = dict()
        self.res = sys.maxsize      
        for source, destination, price in flights:
            prices[source] = prices.get(source, [])
            prices[source].append([destination, price])
        self.dfs(prices, src, dst, 0, K + 1)
        if self.res < sys.maxsize:
            return self.res 
        return -1
    
    def dfs(self, prices, src, dst, cost, k):
        if k < 0:
            return 
        if src == dst:
            self.res = min(self.res, cost)
            return
        if src not in prices:
            return 
        for nxt, price in prices[src]:
            if cost+price > self.res:
                continue
            self.dfs(prices, nxt, dst, cost+price, k-1)
        return