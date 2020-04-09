class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M or not M[0]:
            return 0 
        m, n = len(M), len(M[0])
        dp = [[[0] * 4 for i in range(n)] for j in range(m)]
        x, y, d1, d2 = 0, 0, 0, 0
        for i in range(m):
            for j in range(n):
                if M[i][j] == 0:
                    continue
                # vertical 
                dp[i][j][0] = dp[i - 1][j][0] + 1 if i > 0 else 1 
                y = max(y, dp[i][j][0])
                # horizontal
                dp[i][j][1] = dp[i][j - 1][1] + 1 if j > 0 else 1
                x = max(x, dp[i][j][1])
                # diagonal
                dp[i][j][2] = dp[i - 1][j - 1][2] + 1 if i > 0 and j > 0 else 1
                d1 = max(d1, dp[i][j][2])
                # anti diagonal
                dp[i][j][3] = dp[i - 1][j + 1][3] + 1 if i > 0 and j + 1 < n else 1
                d2 = max(d2, dp[i][j][3])
                
        return max(x, y, d1, d2)
                