class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        result = 0
        def dfs(x, y):
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            count = 1
            for k in range(4):
                nx, ny = dx[k] + x, dy[k] + y
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    count += dfs(nx, ny)
            return count
                
                
        
        m, n = len(grid), len(grid[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    cur = dfs(i, j)
                    result = max(cur, result)
        return result 
        
        