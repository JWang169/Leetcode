class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        self.result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    visited[i][j] = True
                    self.search(grid, i, j, visited, grid[i][j])
                    visited[i][j] = False
        return self.result
    
    def search(self, grid, x, y, visited, cumsum):
        self.result = max(self.result, cumsum)
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                self.search(grid, nx, ny, visited, cumsum + grid[nx][ny])
                visited[nx][ny] = False
        return 
        
        