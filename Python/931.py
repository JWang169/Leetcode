class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        if not A or not A[0]:
            return 0
        m, n = len(A), len(A[0])
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = A[i][j]
                    continue 
                dp[i][j] = dp[i - 1][j] + A[i][j]
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + A[i][j])
                if j + 1 < n:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j + 1] + A[i][j])
        
        
        return min(dp[-1])
        
        
        