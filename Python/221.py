class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        result = 0
        m, n = len(matrix), len(matrix[0])
        old = [0] * n 
        
        for i in range(m):
            new = [0] * n
            for j in range(n):
                if matrix[i][j] == '0':
                    new[j] = 0
                    continue
                if i == 0 or j == 0:
                    new[j] = int(matrix[i][j])
                    result = max(new[j], result)
                    continue
                # matrix[i][j] == 1
                prev = min(old[j], new[j - 1], old[j - 1])
                new[j] = prev + 1 
                result = max(new[j], result)
            old = new
            
        return result * result