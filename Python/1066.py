class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        seen = set()
        heap = [[0, 0, '0'*len(bikes)]]
        while heap:
            # @i: worker idx; 
            # @taken: binary state of all bikes;
            # @cost: distance after assign worker i  
            cost, i, taken = heapq.heappop(heap)
            if(i, taken) in seen:
                continue
            seen.add((i, taken))
            if i == len(workers):
                return cost
            
            for j in range(len(bikes)):
                if taken[j] == '0':
                    dist = self.getDist(workers[i], bikes[j])
                    heapq.heappush(heap, [cost + dist, i + 1, taken[:j] + '1' + taken[j + 1:]])    
        
    def getDist(self, w, b):
        return abs(w[0] - b[0]) + abs(w[1] - b[1])
        

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        self.seen = dict()
        return self.dfs(0, workers, bikes, [0 for _ in range(len(bikes))])
    
    def dfs(self, i, workers, bikes, visited):
        if len(workers) == i:
            return 0
        pair = (i, tuple(visited))
        if pair in self.seen:
            return self.seen[pair]
        
        wx, wy = workers[i]
        dist = sys.maxsize
        for j in range(len(visited)):
            if visited[j] == 1:
                continue
            visited[j] = 1
            bx, by = bikes[j]
            cur = abs(wx - bx) + abs(wy - by)
            dist = min(dist, self.dfs(i + 1, workers, bikes, visited) + cur)       
            visited[j] = 0
            
        self.seen[pair] = dist
        return dist 

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n = len(workers)    
        self.result = sys.maxsize
        self.dfs(workers, bikes, 0)
        return self.result
    
    
    def dfs(self, workers, bikes, dist):
        if not workers:
            self.result = min(self.result, dist)
            return 
        if dist >= self.result:
            return 
        wx, wy = workers[0]
        for i in range(len(bikes)):
            bx, by = bikes[i]
            cur = abs(wx - bx) + abs(wy - by)
            self.dfs(workers[1:], bikes[:i] + bikes[i + 1:], cur + dist)
        return 