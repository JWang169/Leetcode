class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    def longestContinuousIncreasingSubsequence2(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        visited = [[0] * n for _ in range(m)]
        result = 0
        for i in range(m):
            for j in range(n):
                self.dfs(matrix, i, j, visited)
                result = max(result, visited[i][j])
        return result
    
    def dfs(self, matrix, i, j, visited):
        if visited[i][j] != 0:
            return 
        visited[i][j] = 1 
        m, n = len(matrix), len(matrix[0])
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] < matrix[i][j]:
                self.dfs(matrix, nx, ny, visited)
                visited[i][j] = max(visited[i][j], visited[nx][ny] + 1)
  
        
    #     result = 1
    #     visited = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
    #     for i in range(len(matrix)):
    #         for j in range(len(matrix[0])):
    #             if visited[i][j] != -1:
    #                 result = max(visited[i][j], result)
    #                 continue 
    #             self.search(visited, matrix, i, j)
    #             result = max(visited[i][j], result)
    #     return result 
    
    
    # def search(self, visited, matrix, x, y):
    #     visited[x][y] = 1
    #     dx = [0, 0, -1, 1]
    #     dy = [1, -1, 0, 0]
    #     for i in range(4):
    #         nx = dx[i] + x
    #         ny = dy[i] + y
    #         if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and visited[nx][ny] == -1:
    #             if matrix[x][y] > matrix[nx][ny]:
    #                 self.search(visited, matrix, nx, ny)
    #                 visited[x][y] = max(visited[x][y], visited[nx][ny] + 1)
                
                
                