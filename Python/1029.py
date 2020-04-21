class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        heap = []
        for x, y in costs:
            dist = abs(x - y)
            heapq.heappush(heap, (-dist, x, y))
        
        result = 0
        count0 = 0
        count1 = 0
        n = len(costs) // 2
        
        while heap:
            dist, x, y = heapq.heappop(heap)   
            if x < y:
                if count0 < n:
                    count0 += 1
                    result += x
                else:
                    count1 += 1 
                    result += y
            else:
                if count1 < n:
                    count1 += 1
                    result += y
                else:
                    count0 += 1 
                    result += x
        
        return result
        
        
        
        
        
