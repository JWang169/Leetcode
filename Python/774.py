class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        dists = self.getDists(stations)
        left, right = min(dists) / K, max(dists)
        while left + 10e-6  < right:
            print(left, right)
            count = 0
            mid = (left + right) / 2 
            for i in range(len(stations) - 1):
                d = abs(stations[i + 1] - stations[i])
                count += math.ceil(d / mid) - 1
            if count > K :
                left = mid 
            else:
                right = mid 
        
        count = 0
        for i in range(len(stations) - 1):  
            d = abs(stations[i + 1] - stations[i])
            count += math.ceil(d / left)
        if count <= K:
            return left 
        return right 
        
            
            
    def getDists(self, stations):
        dists = []
        for i in range(len(stations) - 1):
            dists.append(abs(stations[i + 1] - stations[i]))
        return dists
            
        
        