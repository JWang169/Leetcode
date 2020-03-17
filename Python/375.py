class Solution:
    def getMoneyAmount(self, n: int) -> int:
        if n <= 1:
            return 0
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        # dp[i][j]: n in [i, j] with i, j both included
        for i in range(n):
            dp[i][i + 1] = i
            
        for length in range(3, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                # k is the last number to guess
                dp[i][j] = sys.maxsize
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], max(dp[i][k - 1], dp[k + 1][j]) + k)
        return dp[1][n]
        