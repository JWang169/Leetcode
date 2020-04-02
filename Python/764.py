# DP 
class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        grid = [[N] * N for _ in range(N)]
    
        for x, y in mines:
            grid[x][y] = 0   
        for i in range(N):
            # left 
            left = 0
            for j in range(N):
                if grid[i][j] != 0:
                    left += 1 
                else:
                    left = 0
                grid[i][j] = min(grid[i][j], left)
            # print(grid)
            right = 0
            for j in range(N - 1, -1, -1):
                if grid[i][j] != 0:
                    right += 1 
                else:
                    right = 0
                grid[i][j] = min(grid[i][j], right)
            up = 0
            for r in range(N):
                if grid[r][i] != 0:
                    up += 1 
                else:
                    up = 0
                grid[r][i] = min(grid[r][i], up)
            down = 0
            for r in range(N - 1, -1, -1):
                if grid[r][i] != 0:
                    down += 1 
                else:
                    down = 0
                grid[r][i] = min(grid[r][i], down)
                
        res = 0
        for i in range(N):
            for j in range(N):
                res = max(res, grid[i][j])
        return res


# BFS TLE
class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        grid = [[1] * N for _ in range(N)]
        for x, y in mines:
            grid[x][y] = 0
        
        queue = deque()
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    queue.append((i, j))
        
        r = 0
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]
        while queue:
            r += 1 
            for i in range(len(queue)):
                x, y = queue.popleft()
                plus = True
                for i in range(4):
                    nx, ny = dx[i] * r + x, dy[i] * r + y
                    if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1:
                        continue 
                    else:
                        plus = False
                        break
                if plus:
                    queue.append((x, y))
        return r
                        
        
        