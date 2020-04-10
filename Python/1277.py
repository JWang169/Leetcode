class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] *(n + 1) for j in range(m + 1)]
        count = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # if 0: no square
                if matrix[i - 1][j - 1] != 0:
                    
                    
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1]))+ 1

                count += dp[i][j]
        return count
                
        
    
                
        
        