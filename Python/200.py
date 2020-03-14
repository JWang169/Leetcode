class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        # self.visited = [[False] * n for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # self.visited[i][j] = True
                    self.search(grid, i, j)
                    count += 1 
        return count 
    
    def search(self, grid, x, y):
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                grid[nx][ny] ='0'
                self.search(grid, nx, ny)
        return 