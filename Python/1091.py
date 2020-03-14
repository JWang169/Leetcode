from collections import deque 
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        self.queue = deque([[0, 0]])
        count = 0
        while self.queue:
            count += 1 
            for i in range(len(self.queue)):
                x, y = self.queue.popleft()
                grid[x][y] = 1
                if x == len(grid) - 1 and y == len(grid[0]) - 1:
                    return count
                dirs = [[-1, 1], [-1, 0], [-1, -1], [0, 1], [0, -1], [1, 1], [1, 0], [1, -1]]
                for dx, dy in dirs:
                    nx, ny = dx + x, dy + y
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0: 
                        grid[nx][ny] = 1
                        self.queue.append([nx, ny])
        return -1
          
    