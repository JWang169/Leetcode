"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
from collections import deque
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        if not grid:
            return -1 
        sx, sy = source.x, source.y 
        dx, dy = destination.x, destination.y 
        
        xx = [1, 1, -1, -1, 2, 2, -2, -2]
        yy = [2, -2, 2, -2, 1, -1, 1, -1]
        if grid[sx][sy] == 1 or grid[dx][dy] == 1:
            return -1
        self.queue = deque()
        count = -1
        self.queue.append((sx, sy))
        while self.queue:
            count += 1 
            for i in range(len(self.queue)):
                x, y = self.queue.popleft()
                if x == dx and y == dy:
                    return count 
                grid[x][y] = 1
                
                for i in range(len(xx)):
                    nx, ny = xx[i] + x, yy[i] + y 
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        self.queue.append((nx, ny))
        
        return -1 
