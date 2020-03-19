class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        f = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    f[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    f[i][j] = 1
                    continue
                if i == 0:
                    f[i][j] = f[i][j - 1]
                elif j == 0:
                    f[i][j] = f[i - 1][j]
                else:
                    f[i][j] = f[i - 1][j] + f[i][j - 1]
                    
        return f[-1][-1]
                    