import heapq
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        self.visited = [[False] * n for _ in range(m)]
        self.total = 0
        self.heap = []
        
        for i in range(m):
            # heights[i][0] & heights[i][n - 1]
            self.visited[i][0] = True 
            self.visited[i][n - 1] = True 
            heapq.heappush(self.heap, (heightMap[i][0], i, 0)) # left column 
            heapq.heappush(self.heap, (heightMap[i][n - 1], i, n - 1)) # right column
        for i in range(n):
            self.visited[0][i] = True
            self.visited[m - 1][i] = True
            heapq.heappush(self.heap, (heightMap[0][i], 0, i)) # first row 
            heapq.heappush(self.heap, (heightMap[m - 1][i], m - 1, i)) # last row
            
        while self.heap:
            curMin = heapq.heappop(self.heap)
            
            self.search(curMin, heightMap, m, n)
        
        return self.total
    
    def search(self, point, heightMap, m, n):
        neighbors = []
        height, x, y = point
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 < nx < m - 1 and 0 < ny < n - 1 and not self.visited[nx][ny]:
                nheight = heightMap[nx][ny]
                self.visited[nx][ny] = True 
                if nheight < height:
                    self.total += height - nheight  
                heapq.heappush(self.heap, (max(nheight, height), nx, ny))