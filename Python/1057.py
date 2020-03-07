import heapq
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        heap = []
        dists = dict()
        for i in range(len(workers)):
            dists[i] = []
            for j in range(len(bikes)):
                dist = abs(bikes[j][0] - workers[i][0]) + abs(bikes[j][1] - workers[i][1]) 
                heapq.heappush(dists[i], (dist, i, j))
        
        for i in range(len(workers)):
            heapq.heappush(heap, heapq.heappop(dists[i]))    
        result = [0] * len(workers)
        assignedBikes = set()
        assignedWorkers = set()
        while len(assignedWorkers) < len(workers):
            dist, w, b = heapq.heappop(heap)
            if b not in assignedBikes and w not in assignedWorkers:
                result[w] = b
                assignedBikes.add(b)
                assignedWorkers.add(w)
            else:
                heapq.heappush(heap, heapq.heappop(dists[w]))
      
        return result