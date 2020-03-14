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
        # write your code here
        dirs = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
        if not grid or not grid[0]:
            return -1
        sx, sy = source.x, source.y
        tx, ty = destination.x, destination.y 
        if grid[sx][sy] == 1 or grid[tx][ty] == 1:
            return -1 
        count = 0
        queue = deque([[sx, sy]])
        while queue:
            for i in range(len(queue)):
                x, y = queue.popleft()
                if x == tx and y == ty:
                    return count 
                grid[x][y] = 1 
                for dx, dy in dirs:
                    nx, ny = dx + x, dy + y 
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                        queue.append([nx, ny])
                        grid[nx][ny] = 1 
            count += 1 
        return -1