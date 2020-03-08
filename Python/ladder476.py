import sys 
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        n = len(A)
        if n < 2:
            return 0
        
        # dp[i][j]: minimum cost merge from i to j 
        dp = [[0] * n for _ in range(n)]
        # rangeSum[i][j] = A[i] + A[i + 1] + ... + A[j]
        
        rangeSum = self.getRangeSum(A)
        # enumerate length
        for length in range(2, n + 1 ):
            for i in range(n - length + 1 ):     # left 
                j = i + length - 1           # right 
                dp[i][j] = sys.maxsize
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + rangeSum[i][j])
        return dp[0][n - 1]
        
        
    def getRangeSum(self, A):
        n = len(A) 
        rangeSum = [[0] * n for _ in range(n)]
        # rangeSum[i][j] : sum(A[i: j + 1])
        for i in range(n):
            rangeSum[i][i] = A[i]
            for j in range(i + 1, n):
                rangeSum[i][j] = rangeSum[i][j - 1] + A[j]
        return rangeSum 
            
        