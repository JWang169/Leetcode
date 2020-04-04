class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        dist = []
        pp = [p1, p2, p3, p4]
        for i in range(3):
            for j in range(i + 1, 4):
                x0, y0 = pp[i]
                x1, y1 = pp[j]
                dist.append((x0 - x1) ** 2 + (y0 - y1) ** 2)
        
        dist.sort()
        print(dist)
        if dist[0] == dist[1] and dist[1] == dist[2] and dist[2] == dist[3] and dist[4] == dist[5] and dist[5] > dist[0] and dist[0] + dist[3] == dist[5]:
            return True 
        return False 
        
        
        
        