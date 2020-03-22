from collections import deque
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        paths = {1:[[0, 1], [0, -1]], 2: [[1, 0], [-1, 0]], 3: [[0, -1], [1, 0]], 4:[[1, 0], [0, 1]], 5:[[0, -1], [-1, 0]], 6:[[0, 1], [-1, 0]]}
        pairs = {(0, 1) : [1, 3, 5], (0, -1): [1, 4, 6], (1, 0): [2, 5, 6], (-1, 0): [2, 3, 4]}
        tx, ty = len(grid) - 1, len(grid[0]) - 1
        queue = deque()
        queue.append([0, 0])
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        start = [0, 0]    
        
        while queue:
            x, y = queue.popleft()
            if x == tx and y == ty:
                return True
            num = grid[x][y]
            visited[x][y] = True 
            for dx, dy in paths[num]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    nxt = pairs[(dx, dy)]
                    if grid[nx][ny] in nxt and not visited[nx][ny]:
                        queue.append([nx, ny])
            
        return False 
                    
                
            
        